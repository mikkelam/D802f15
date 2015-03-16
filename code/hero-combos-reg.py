import json
import sys
sys.path.append()
import glob
from pyspark import SparkContext
from pyspark.mllib.classification import LogisticRegressionWithSGD
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import SparseVector


def _get_teams(match):
	team1 = []
	team2 = []
	champions = [266, 103, 84, 12, 32, 34, 1, 22, 268, 53, 63, 201, 51, 69, 31, 42, 122, 131, 36, 119, 60, 28, 81, 9, 114, 105, 3, 41, 86, 150, 79, 104, 120, 74, 39, 40, 59, 24, 126, 222, 429, 43, 30, 38, 55, 10, 85, 121, 96, 7, 64, 89, 127, 236, 117, 99, 54, 90, 57, 11, 21, 82, 25, 267, 75, 111, 76, 56, 20, 2, 61, 80, 78, 133, 33, 421, 58, 107, 92, 68, 13, 113, 35, 98, 102, 27, 14, 15, 72, 37, 16, 50, 134, 91, 44, 17, 412, 18, 48, 23, 4, 29, 77, 6, 110, 67, 45, 161, 254, 112, 8, 106, 19, 62, 101, 5, 157, 83, 154, 238, 115, 26, 143]
	team2_offset = len(champions)
	for participant in match["participants"]:
		champion_id = champions.index(participant["championId"])
		if participant["teamId"] == 100:
			team1.append(champion_id)
		if participant["teamId"] == 200:
			team2.append(champion_id)
	team1.sort() 
	team2.sort()
	return (team1, team2)
	
def _get_team_combos(team1, team2, cross_team=False): 
	combos = []
	for champion1 in team1:
		for champion2 in team2:
			if cross_team:
				combos.append((champion1, champion2))
			else:
				if champion1 < champion2:
					combos.append((champion1, champion2))
	return combos
	
	
def _get_combo_list(offset, team1, team2, number_of_champions, cross_team=False):
	combos = _get_team_combos(team1, team2, cross_team) #finds the combos of the teams
	feature_list = []
	for combo in combos: 
		if len(combo) == 2 and not cross_team: #The combo list is a list of combos within a team
			champ1_id, champ2_id = combo
			combo_index = offset+(champ1_id*(2*number_of_champions-1-champ1_id))/2+champ2_id-(champ1_id+1) #Implementation of offset+x(2n-1-x)/2+y-(x+1)
		elif len(combo) == 2 and cross_team: #The combo list is a list of crossteam combos 
			champ1_id, champ2_id = combo
			combo_index = offset+champ1_id*(number_of_champions)+champ2_id # Implementation of offset+x*n+y
		feature_list.append(combo_index)
	return feature_list


# Load and parse the data
def parsePoint(line):
	line_data = json.loads(line)
	team1, team2 = _get_teams(line_data)
	offset_team1_combo, offset_team2_combo, offset_crossteam_combo, num_of_champs = (246, 7749, 15252, 123)
	team1_combo_list = _get_combo_list(offset_team1_combo, team1, team1, num_of_champs, False) #list of the combos on team1
	team2_combo_list = _get_combo_list(offset_team2_combo, team2, team2, num_of_champs, False) #list of the combos on team2
	cross_team_combo_list = _get_combo_list(offset_crossteam_combo, team1, team2, num_of_champs, True) #list of the cross team combos
	game_result = 0.0
	if line_data["teams"][0]["winner"]:
		game_result = 1.0
		
	#Adds offset to team2 
	team2 = [num_of_champs + champ_id for champ_id in team2]
	
	#Combine all feature list to a feature list
	feature_list = team1+team2+team1_combo_list+team2_combo_list+cross_team_combo_list
	features = {}
	for feature in feature_list:
		features[feature] = 1
	return LabeledPoint(game_result, SparseVector(30381, features)) #values in the feature vector are too large, 30381

def matchfilter(x):
	try:
		json_object = json.loads(x)
		if json_object["queueType"] == "RANKED_SOLO_5x5":
			return True
	except:
		return False
	return False

sc = SparkContext("local", "Simple App")
data = sc.textFile(','.join(glob.glob('/Users/andreaseriksen/Desktop/Project F15/code/data/traning/*.txt')))
eval_data = sc.textFile(','.join(glob.glob('/Users/andreaseriksen/Desktop/Project F15/code/data/eval/*.txt')))

traning_data, eval_data = data.filter(lambda line: matchfilter(line)).randomSplit([0.9, 0.1], 1)

parsedData = traning_data.map(parsePoint)

# Build the model
model = LogisticRegressionWithSGD.train(parsedData)



# Evaluating the model on evaluation data
eval_parsedData = eval_data.map(parsePoint)
labelsAndPreds = eval_parsedData.map(lambda p: (p.label, model.predict(p.features)))
trainErr = labelsAndPreds.filter(lambda (v, p): v != p).count()

eval_count = eval_parsedData.count()
test_count = parsedData.count()
#print float(eval_parsedData.count())
print("Training Error = " + str(trainErr))


print "eval", eval_count
print "test", test_count
#data = []
#for file in os.listdir("/Users/andreaseriksen/Desktop/Project F15/code/data/subset"):
#	if file.endswith(".txt"):
#		print file
#		with open("/Users/andreaseriksen/Desktop/Project F15/code/data/subset/" + file, 'r') as f:
#			for line in f:
#				try:
#					d = json.loads(line)
#					data.append(d)
#				except:
#					print "Error in line"
#		f.close()
#team1, team2 = get_teams(data[0])
#print team1, team2
#combos = get_team_combos(team1, team2, True)
#feature_list = get_feature_list(15252, combos, 123, True)
#print feature_list
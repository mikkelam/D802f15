from pyspark.mllib.classification import LogisticRegressionWithSGD
from pyspark.mllib.regression import LabeledPoint
from numpy import array
from pyspark import SparkContext
import json
import glob
from utility.utility import champion_index
from matchfilter.matchfilter import MatchFilter

# Load and parse the data
def parse_point(line):
	
	#load the json scheme, if the json is not valid, an exception is thrown.
	try:
		json_object = json.loads(line)
	except ValueError, ex_mathias:
		print "json object is not valid"

	featureList = [0] * 247 # a list of zeros. index 0 is the label/class, followed by the featurelist
	for p in json_object[ "participants" ]:
		champIndex = 1 # index 0 must be the label
		champIndex += champion_index(p[ "championId" ])
		if p[ "teamId" ] == 200:
			champIndex += 123 # first 123 is team blue, following 123 is team red
		featureList[champIndex] = 1
	if json_object["participants"][0]["stats"]["winner"] == True: ####!!!!! this never evaluate to true
		featureList[0] = 1
	return LabeledPoint(featureList[0], featureList[1:]) #LbabeledPoint is imported

def filter_lines(line):
	#load the json scheme, if the json is not valid, an exception is thrown.
	try:
		json_object = json.loads(line)
	except ValueError, exJson:
		print "json object is not valid"
		return False
	mf = MatchFilter() #filter the match, following the MatchFilter class
	return mf.passes(json_object)

def hero_team_win():
	sc = SparkContext("local", "Simple App")
	data = sc.textFile(','.join(glob.glob('../LoLMiner/LoLMiner/src/mined-data/region-euw-start-1971603524-size-1000.txt')))  #"data.txt")

	#filter data
	filteredData = data.filter(filter_lines)
	
	#randomSplit() the data into training and test sets
	trainData, evaluateData = filteredData.randomSplit([0.8, 0.2], 1) #train size, eval size, seed number

	#train the model
	parsedTrainData = trainData.map(parse_point)
	model = LogisticRegressionWithSGD.train(parsedTrainData, iterations=10, regParam=0.01, regType="l1")
	
	# Evaluating the model on evaluate data
	parsedEvaluateData = evaluateData.map(parse_point)
	labelsAndPreds = parsedEvaluateData.map(lambda p: (p.label,  model.predict(p.features)))
	trainErr = labelsAndPreds.filter(lambda (v, p): v != p).count() / float(parsedEvaluateData.count())
	
	# print("Lines of training json: " + str( (parsedTrainData.count() ))) 
	# print("Lines of evaluate json: " + str( (parsedEvaluateData.count() )))
	print("Training Error = " + str(trainErr))
from pyspark.mllib.classification import LogisticRegressionWithSGD
from pyspark.mllib.regression import LabeledPoint
from numpy import array
from pyspark import SparkContext
#from MatchFilter import MatchFilter
import json
import glob

sc = SparkContext("local", "Simple App")

# Return the featurelist index of a given champ+team
def championIndex(championId, team):
	championList = [266, 103, 84, 12, 32, 34, 1, 22, 268, 53, 63, 201, 51, 69, 31, 42, 122, 131, 36, 119, 60, 28, 81, 9, 114, 105, 3, 41, 86, 150, 79, 104, 120, 74, 39, 40, 59, 24, 126, 222, 429, 43, 30, 38, 55, 10, 85, 121, 96, 7, 64, 89, 127, 236, 117, 99, 54, 90, 57, 11, 21, 82, 25, 267, 75, 111, 76, 56, 20, 2, 61, 80, 78, 133, 33, 421, 58, 107, 92, 68, 13, 113, 35, 98, 102, 27, 14, 15, 72, 37, 16, 50, 134, 91, 44, 17, 412, 18, 48, 23, 4, 29, 77, 6, 110, 67, 45, 161, 254, 112, 8, 106, 19, 62, 101, 5, 157, 83, 154, 238, 115, 26, 143]
	if team == 100:
		return championList.index(championId)
	else: #team == 200
		return championList.index(championId) + 123

# Load and parse the data
def parsePoint(line):
	json_object = json.loads(line)
	#if MatchFilter.passes(json_object):
	featureList = [0] * 247 # a list of zeros. index 0 is the label/class, followed by the featurelist
	for p in json_object[ "participants" ]:
		champIndex = championIndex(p[ "championId" ], p[ "teamId" ]) + 1 #add one, as index 0 is the label, not a feature
		featureList[champIndex] = 1
	if json_object["participants"][0]["stats"]["winner"] == "true":
		featureList[0] = 1
	return LabeledPoint(featureList[0], featureList[1:]) #LbabeledPoint is imported

data = sc.textFile(','.join(glob.glob('../LoLMiner/LoLMiner/src/mined-data/region-euw-start-1971603524-size-1000.txt')))  #"data.txt")
parsedData = data.map(parsePoint)
model = LogisticRegressionWithSGD.train(parsedData)

# Evaluating the model on training data
labelsAndPreds = parsedData.map(lambda p: (p.label,  model.predict(p.features)))
trainErr = labelsAndPreds.filter(lambda (v, p): v != p).count() / float(parsedData.count())
print("lines of json: " + str(parsedData.count()))
print("Training Error = " + str(trainErr))




import json
import os
import glob 
import sys
import csv

from pyspark import SparkContext
from pyspark.mllib.classification import LogisticRegressionWithSGD
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import SparseVector
from prediction.matchfilter import MatchFilter


champion_ids = [266, 103, 84, 12, 32, 34, 1, 22, 268, 53, 63, 201, 51, 69, 31, 42, 122, 131, 36, 119, 60, 28, 81, 9, 114, 105, 3, 41, 86, 150, 79, 104, 120, 74, 39, 40, 59, 24, 126, 222, 429, 43, 30, 38, 55, 10, 85, 121, 96, 7, 64, 89, 127, 236, 117, 99, 54, 90, 57, 11, 21, 82, 25, 267, 75, 111, 76, 56, 20, 2, 61, 80, 78, 133, 33, 421, 58, 107, 92, 68, 13, 113, 35, 98, 102, 27, 14, 15, 72, 37, 16, 50, 134, 91, 44, 17, 412, 18, 48, 23, 4, 29, 77, 6, 110, 67, 45, 161, 254, 112, 8, 106, 19, 62, 101, 5, 157, 83, 154, 238, 115, 26, 143, 432]


mf = MatchFilter({"matchMode": ["CLASSIC"],
	                          "matchType": ["MATCHED_GAME"],
	                          "queueType": ["RANKED_SOLO_5x5", "RANKED_PREMADE_5x5", "NORMAL_5x5_BLIND", "NORMAL_5x5_DRAFT"],
	                          "participants->*->timeline->xpPerMinDeltas->*": ["!0"]})
	
def matchfilter(line):
	try:
		json_object = json.loads(line)
		if mf.passes(json_object):
			return True
	except:
		print "Invalid json"
		return False
	return False
		

def feature_creator(match, features, team):
	ids = []
	if team == 100:
		label = match["teams"][0]["winner"]
	elif team == 200:
		label = not match["teams"][0]["winner"]
		
	if features == "single":
		for participant in match["participants"]:
			if participant["teamId"] == 100:
				ids.append(champion_ids.index(participant["championId"]))
			if participant["teamId"] == 200:
				ids.append(champion_ids.index(participant["championId"])+len(champion_ids))
	if features == "multi":
		for participant in match["participants"]:
			if participant["teamId"] == team:
				ids.append(champion_ids.index(participant["championId"]))
	return (label, ids)
		
# Load and parse the data
def parsePoint(single_match, features, redlabel=False):
	#Generates the features of the game
	match = json.loads(single_match)
	if redlabel:
		(label, ids) = 	feature_creator(match, features, 200)
	else:
		(label, ids) = feature_creator(match, features, 100)
	
	#Creates the input to a sparce vector from the feature creator
	features = {}
	for feature in ids:
		features[feature] = 1 
	
	return LabeledPoint(int(label), SparseVector(300, features)) 
	
	# Load and parse the data

	
sc = SparkContext("local", "Simple App")
data = sc.textFile(','.join(glob.glob('/Users/andreaseriksen/Desktop/Project F15/code/data/traning/*.txt')))

traning_data, eval_data = data.filter(lambda line: matchfilter(line)).randomSplit([0.9, 0.1], 1)


blueparsedData = traning_data.map(lambda line: parsePoint(line,"multi"))
redparsedData = traning_data.map(lambda line: parsePoint(line, "multi", True))
blueeval = eval_data.map(lambda line: parsePoint(line, "multi"))
redeval = eval_data.map(lambda line: parsePoint(line, "multi", True))
doubleparsedData = blueparsedData.union(redparsedData)
doubleeval = blueeval.union(redeval)

#redparsedData
# Build the model

parsedData = traning_data.map(lambda line: parsePoint(line, "single"))
singleeval = eval_data.map(lambda line: parsePoint(line, "single"))

outputpath ="/Users/andreaseriksen/Desktop/Project F15/code/data/eval/"


doublemodel = LogisticRegressionWithSGD.train(doubleparsedData)
singlemodel = LogisticRegressionWithSGD.train(parsedData)


def __eval__(parsedData, model, name):
	count = parsedData.count()
	#print float(eval_parsedData.count())
	prediction = parsedData.map(lambda p: (p.label,  model.predict(p.features)))
	error = prediction.filter(lambda (v, p): v != p).count()
	
	outputpath ="/Users/andreaseriksen/Desktop/Project F15/code/data/eval/"

	file = open(outputpath + name + ".txt",'w')
	file.write("count: " + str(count) + "\n")
	file.write("prediction error: " + str(error)+"\n")
	file.close()
	
__eval__(singleeval, singlemodel, "singlepoint_test_eval")
__eval__(doubleeval, doublemodel, "doublepoint_test_eval")
import json
import os
import glob 
import sys
import csv
from collections import OrderedDict
from pyspark import SparkContext
from pyspark.mllib.classification import LogisticRegressionWithSGD
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import SparseVector
from featurecreator import *


def matchfilter(line):
	try:
		json_object = json.loads(line)
		return True
	except:
		print "Invalid json"
		return False

# Load and parse the data
def parsePoint(single_match, testfeatures, feature_creator, redlabel=False):
	#Generates the features of the game
	match = json.loads(single_match)
	feature_creator.set_match(match)
	
	for feature in testfeatures:
		feature_creator.make_features(feature)
	
	#Creates the input to a sparce vector from the feature creator
	features = {}
	for feature in feature_creator.current_match_features:
		features[feature] = 1 
	
	label = feature_creator.label
	if redlabel:
		label = not label
	return LabeledPoint(int(label), SparseVector(3000, features)) 
	
	# Load and parse the data

	
sc = SparkContext("local", "Simple App")
data = sc.textFile(','.join(glob.glob('/Users/andreaseriksen/Desktop/Project F15/code/data/traning/*.txt')))

traning_data, eval_data = data.filter(lambda line: matchfilter(line)).randomSplit([0.9, 0.1], 1)

fc = FeatureCreator()
blueparsedData = traning_data.map(lambda line: parsePoint(line, [FeatureType.BLUE_TEAM_SINGLES], fc))
redparsedData = traning_data.map(lambda line: parsePoint(line, [FeatureType.RED_TEAM_SINGLES], fc, True))
blueeval = eval_data.map(lambda line: parsePoint(line, [FeatureType.BLUE_TEAM_SINGLES], fc))
redeval = eval_data.map(lambda line: parsePoint(line, [FeatureType.RED_TEAM_SINGLES], fc, True))
doubleparsedData = blueparsedData.union(redparsedData)
doubleeval = blueeval.union(redeval)

#redparsedData
# Build the model
fc = FeatureCreator()
parsedData = traning_data.map(lambda line: parsePoint(line, [FeatureType.BLUE_TEAM_SINGLES,FeatureType.RED_TEAM_SINGLES], fc))
singleeval = eval_data.map(lambda line: parsePoint(line, [FeatureType.BLUE_TEAM_SINGLES,FeatureType.RED_TEAM_SINGLES], fc))

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
	#print("Training Error = " + str(trainErr))

	#print "test", test_count
	##data = []
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

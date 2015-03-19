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
def parsePoint(single_match):
	#Generates the features of the game
	feature_creator = FeatureCreator()
	feature_creator.set_match(single_match)
	feature_creator.make_features(FeatureType.FIRST_BLOOD)
	feature_creator.make_features(FeatureType.RED_TEAM_SINGLES)
	feature_creator.make_features(FeatureType.BLUE_TEAM_SINGLES)
	feature_creator.make_features(FeatureType.RED_TEAM_PAIRS)
	feature_creator.make_features(FeatureType.BLUE_TEAM_PAIRS)
	#Creates the input to a sparce vector from the feature creator
	features = {}
	for feature in feature_creator.sparse_feature_list:
		features[feature] = 1 
	
	return LabeledPoint(int(feature_creator.label), SparseVector(feature_creator.feature_count, features)) 
	
sc = SparkContext("local", "Simple App")
data = sc.textFile(','.join(glob.glob('/Users/andreaseriksen/Desktop/Project F15/code/data/traning/*.txt')))

traning_data, eval_data = data.filter(lambda line: matchfilter(line)).randomSplit([0.9, 0.1], 1)

parsedData = traning_data.map(parsePoint)

# Build the model

model = LogisticRegressionWithSGD.train(parsedData)


test_count = parsedData.count()
#print float(eval_parsedData.count())
print test_count
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

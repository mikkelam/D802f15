import json
import os
from featurecreator import *
from WekaConverter import WekaConverter
inputpath = r"/Users/andreaseriksen/Desktop/Project F15/code/data/"

feature_creator_blue = FeatureCreator()
feature_creator_red = FeatureCreator()
number_of_features = feature_creator_blue.champion_count+1
wc = WekaConverter(number_of_features, path="/Users/andreaseriksen/Desktop/Project F15/code/data/subset/10000Games.arff")
games_to_extract = 10000

for f in os.listdir(inputpath):
	if not f.endswith(".txt"):
		continue
	if games_to_extract == 0:
		break
	with open(inputpath + f, 'r') as file:
		for line in file:
			games_to_extract -= 1
			print (games_to_extract)
			try:
				single_match = json.loads(line)
			except:
				print "invalid json"
				continue
			feature_creator_blue.set_match(single_match)
			feature_creator_blue.make_features(FeatureType.BLUE_TEAM_SINGLES)
			feature_creator_red.set_match(single_match)
			feature_creator_red.make_features(FeatureType.RED_TEAM_SINGLES)
			wc.add(feature_creator_blue.sparse_feature_list, feature_creator_blue.label)
			wc.add(feature_creator_red.sparse_feature_list, not feature_creator_red.label)
			print ("Label: " + str(feature_creator_blue.label) + " Features: " + str(feature_creator_blue.sparse_feature_list))
			print ("Label: " + str(not feature_creator_red.label) + " Features: " + str(feature_creator_red.sparse_feature_list))
wc.write()


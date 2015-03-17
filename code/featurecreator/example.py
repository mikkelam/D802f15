import json
import os
from featurecreator import *
path = r"/Users/andreaseriksen/Desktop/Project F15/code/data/subset/region-euw-start-1971861776-size-1000.txt"

feature_creator = FeatureCreator()

games_to_extract = 100
with open(path, "r") as file:
    for line in file:
        games_to_extract -= 1
        if games_to_extract == 0:
            break
        try:
            single_match = json.loads(line)
        except:
	        print "invalid json"
        feature_creator.set_match(single_match)
        feature_creator.make_features(FeatureType.FIRST_BLOOD)
        feature_creator.make_features(FeatureType.RED_TEAM_SINGLES)
        feature_creator.make_features(FeatureType.BLUE_TEAM_SINGLES)
        feature_creator.make_features(FeatureType.RED_TEAM_PAIRS)
        feature_creator.make_features(FeatureType.BLUE_TEAM_PAIRS)
        print ("Label: " + str(feature_creator.label) + " Features: " + str(feature_creator.sparse_feature_list))

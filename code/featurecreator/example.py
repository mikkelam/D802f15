import json
import os
from featurecreator import *

from WekaConverter import WekaConverter

inputpath = r"C:/Users/Kent/Desktop/D802f15/LoLMiner/LoLMiner/bin/mined-data/" #Path to input files
outputpath = r"C:/Users/Kent/Desktop/testfiles/output.arff" #path to the output file

feature_creator = FeatureCreator()
wc = WekaConverter(outputpath)
games_to_extract = 10000

for f in os.listdir(inputpath):
    if not f.endswith(".txt"):
        continue
    if games_to_extract < 0:
        break
    with open(inputpath + f, 'r') as file:
        for line in file:
            games_to_extract -= 1
            if games_to_extract < 0:
                break
            print (games_to_extract)
            try:
                single_match = json.loads(line)
            except:
                print("invalid json")
                continue
            feature_creator.set_match(single_match)
            feature_creator.make_features(FeatureType.FIRST_TOWER)
            feature_creator.make_features(FeatureType.FIRST_BLOOD)
            feature_creator.make_features(FeatureType.FIRST_DRAGON)
            feature_creator.make_features(FeatureType.FIRST_INHIBITOR)
            feature_creator.make_features(FeatureType.FIRST_BARON)
            feature_creator.make_features(FeatureType.BLUE_TEAM_SINGLES)
            feature_creator.make_features(FeatureType.RED_TEAM_SINGLES)
            wc.add(feature_creator.current_match_features, feature_creator.label)
            print ("Label: " + str(feature_creator.label) + " Features: " + str(feature_creator.current_match_features))
wc.set_feature_names(feature_creator.get_all_feature_names())
wc.write()

#games_to_extract = 100
#with open(path, "r") as file:
#    for line in file:
#        games_to_extract -= 1
#        if games_to_extract == 0:
#            break
#        try:
#            single_match = json.loads(line)
#       except:
#	        print ("invalid json")
 #       feature_creator.set_match(single_match)
#        feature_creator.make_features(FeatureType.FIRST_BLOOD)
#        feature_creator.make_features(FeatureType.FIRST_TOWER)
#        feature_creator.make_features(FeatureType.FIRST_INHIBITOR)
#        feature_creator.make_features(FeatureType.FIRST_DRAGON)
#        feature_creator.make_features(FeatureType.FIRST_BARON)
#        feature_creator.make_features(FeatureType.RED_TEAM_SINGLES)
#        feature_creator.make_features(FeatureType.BLUE_TEAM_SINGLES)
#        feature_creator.make_features(FeatureType.RED_TEAM_PAIRS)
#        feature_creator.make_features(FeatureType.BLUE_TEAM_PAIRS)
#        print ("Label: " + str(feature_creator.label) + " Features: " + str(feature_creator.sparse_feature_list))


import json
import os
from prediction.matchfilter import MatchFilter
from featurecreator import *
from wekaconverter import *

inputpath = r"C:/Users/Kent/Desktop/D802f15/LoLMiner/LoLMiner/bin/mined-data/" #Path to input files
outputpath = r"C:/Users/Kent/Desktop/testfiles/output.arff" #path to the output file

mf = MatchFilter({"matchMode": ["CLASSIC"],
                          "matchType": ["MATCHED_GAME"],
                          "queueType": ["RANKED_SOLO_5x5", "RANKED_PREMADE_5x5", "NORMAL_5x5_BLIND", "NORMAL_5x5_DRAFT"],
                          "participants->*->timeline->xpPerMinDeltas->*": ["!0"]})

feature_creator = FeatureCreator()
feature_types = [FeatureType.BLUE_TEAM_SINGLES,
                 FeatureType.RED_TEAM_SINGLES]
feature_creator.set_feature_types(feature_types)
wc = WekaConverter(outputpath)
games_to_extract = 50000
for f in os.listdir(inputpath):
    if not f.endswith(".txt"):
        continue
    with open(inputpath + f, 'r', encoding="latin-1") as file:
        for line in file:
            if games_to_extract <= 0:
                break
            try:
                single_match = json.loads(line)
            except:
                print("invalid json")
                continue
            if not mf.passes(single_match):
                continue
            feature_creator.set_match(single_match)
            wc.add(feature_creator.current_match_features, feature_creator.label)
            games_to_extract -= 1
            print ("Label: " + str(feature_creator.label) + " Features: " + str(feature_creator.current_match_features))
            print ("Games to extract: " + str(games_to_extract))
wc.set_feature_names(feature_creator.get_all_feature_names())
wc.write()
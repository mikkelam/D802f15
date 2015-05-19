import json
import io
from prediction.matchfilter import MatchFilter
from featurecreator import *
from wekaconverter import *

inputpath = r"C:/Users/Kent/Desktop/D802f15/LoLMiner/LoLMiner/bin/mined-data/" #Path to input files
outputpath1 = r"C:/Users/Kent/Desktop/testfiles/LANE_RANK_VS_RANK/all.arff" #path to the output file

mf = MatchFilter({"matchMode": ["CLASSIC"],
                          "matchType": ["MATCHED_GAME"],
                          "queueType": ["RANKED_SOLO_5x5", "RANKED_PREMADE_5x5", "NORMAL_5x5_BLIND", "NORMAL_5x5_DRAFT"],
                          "participants->*->timeline->xpPerMinDeltas->*": ["!0"]})
#mf.set_min_avg_rank(0.175) # [0.0-1.0] - 0 extracts all, 1.0 only pure challengers. unranked = bronze

feature_creator1 = FeatureCreator()
feature_creator1.set_feature_types([FeatureType.LANE_RANK_VS_RANK])
wc1 = WekaConverter(outputpath1)
games_to_extract = 60000
for f in os.listdir(inputpath):
    if not f.endswith(".json"):
        continue
    with io.open(inputpath + f, 'r', encoding="latin-1") as file:
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
            feature_creator1.set_match(single_match)
            wc1.add(feature_creator1.current_match_features, feature_creator1.label)
            games_to_extract -= 1
            print ("Games to extract: " + str(games_to_extract))
wc1.set_feature_names(feature_creator1.get_all_feature_names())
wc1.write()
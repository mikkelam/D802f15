from spark_feature_test import SparkFeatureTest
from pyspark import SparkContext
from featurecreator.featurecreator import FeatureType
from prediction.matchfilter import MatchFilter

team_features = [FeatureType.BLUE_TEAM_SINGLES, FeatureType.RED_TEAM_SINGLES]
combo_features = [FeatureType.BLUE_TEAM_PAIRS, FeatureType.RED_TEAM_PAIRS]

mf = MatchFilter({"matchMode": ["CLASSIC"],
	                          "matchType": ["MATCHED_GAME"],
	                          "queueType": ["RANKED_SOLO_5x5", "RANKED_PREMADE_5x5", "NORMAL_5x5_BLIND", "NORMAL_5x5_DRAFT", "GROUP_FINDER_5x5"],
	                          "participants->*->highestAchievedSeasonTier": ["MASTER", "CHALLENGER", "DIAMOND", "PLATINUM", "GOLD", "SILVER", "BRONZE", "UNRANKED"] ,
	                          "participants->*->timeline->xpPerMinDeltas->*": ["!0"]})
	

	
outputpath ="/Users/andreaseriksen/Desktop/Project F15/code/data/eval/"
inputpath = "/Users/andreaseriksen/Desktop/Project F15/code/data/valid/"

sc = SparkContext("local", "Simple App")

sft = SparkFeatureTest(outputpath, inputpath, mf)

#sft.run("singleline_team", team_features, sc)
sft.run("singleline_combo", combo_features, sc)
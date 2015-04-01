from sparkfeaturetest import SparkFeatureTest
from pyspark import SparkContext
from featurecreator.featurecreator import FeatureType
from prediction.matchfilter import MatchFilter

team_features = [FeatureType.BLUE_TEAM_SINGLES, FeatureType.RED_TEAM_SINGLES]
combo_features = [FeatureType.BLUE_TEAM_PAIRS, FeatureType.RED_TEAM_PAIRS]
team_combo = [FeatureType.BLUE_TEAM_SINGLES, FeatureType.RED_TEAM_SINGLES, FeatureType.BLUE_TEAM_PAIRS, FeatureType.RED_TEAM_PAIRS]
team_combo_cross = [FeatureType.BLUE_TEAM_SINGLES, FeatureType.RED_TEAM_SINGLES, FeatureType.BLUE_TEAM_PAIRS, FeatureType.RED_TEAM_PAIRS, FeatureType.CROSS_TEAM_PAIRS]
team_crossteam = [FeatureType.BLUE_TEAM_SINGLES, FeatureType.RED_TEAM_SINGLES, FeatureType.CROSS_TEAM_PAIRS]

mf = MatchFilter({"matchMode": ["CLASSIC"],
	                          "matchType": ["MATCHED_GAME"],
	                          "queueType": ["RANKED_SOLO_5x5", "RANKED_PREMADE_5x5", "NORMAL_5x5_BLIND", "NORMAL_5x5_DRAFT"],
	                          "participants->*->timeline->xpPerMinDeltas->*": ["!0"]})

	
outputpath ="/Users/andreaseriksen/Desktop/Project F15/code/data/eval/"
inputpath = "/Users/andreaseriksen/Downloads/test/"

sc = SparkContext("local", "Simple App")

sft = SparkFeatureTest(outputpath, inputpath, mf)

sft.run("spark_single_team", team_features, sc)
#sft.run("combos", combo_features, sc)
#sft.run("teams_combos", team_combo, sc)
#sft.run("team_combo_cross", team_combo_cross, sc)
#sft.run("team_crossteam", team_crossteam, sc)
from sparkfeaturetest import SparkFeatureTest
from pyspark import SparkContext
from featurecreator.featurecreator import FeatureType
from prediction.matchfilter import MatchFilter




mf = MatchFilter({"matchMode": ["CLASSIC"],
	                          "matchType": ["MATCHED_GAME"],
	                          "queueType": ["RANKED_SOLO_5x5", "RANKED_PREMADE_5x5", "NORMAL_5x5_BLIND", "NORMAL_5x5_DRAFT"],
	                          "participants->*->timeline->xpPerMinDeltas->*": ["!0"]})

	
outputpath ="/Users/mikkel/Documents/output/"
inputpath = "/Users/mikkel/Documents/input/"


sc = SparkContext("local")
sft = SparkFeatureTest(outputpath, inputpath, mf)

sft.run("blue_red_team_singlses", [FeatureType.LANE_CHAMPION_COMBO], sc, 1)
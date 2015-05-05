from sparkfeaturetest import SparkFeatureTest
from pyspark import SparkContext
from featurecreator.featurecreator import FeatureType
from prediction.matchfilter import MatchFilter
from pyspark.mllib.classification import LogisticRegressionWithSGD




mf = MatchFilter({"matchMode": ["CLASSIC"],
	                          "matchType": ["MATCHED_GAME"],
	                          "queueType": ["RANKED_SOLO_5x5", "RANKED_PREMADE_5x5", "NORMAL_5x5_BLIND", "NORMAL_5x5_DRAFT", "GROUP_FINDER_5x5"],
	                          "participants->*->timeline->xpPerMinDeltas->*": ["!0"]})

	
outputpath ="/Users/andreaseriksen/Desktop/Project F15/code/data/valid/eval/"
inputpath = "/Users/andreaseriksen/Desktop/Project F15/code/data/valid/*.txt"


sc = SparkContext("local")
sft = SparkFeatureTest(outputpath, inputpath, mf)

sft.run("blue_red_team_singlses", [FeatureType.BLUE_TEAM_SINGLES, FeatureType.RED_TEAM_SINGLES], sc, LogisticRegressionWithSGD,  1.0, 3)
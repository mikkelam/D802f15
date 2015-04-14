import json
import glob

from pyspark import SparkContext
from featurecreator.featurecreator import *
from featurecreator.WekaConverter import WekaConverter
from prediction.matchfilter import MatchFilter

inputpath = "/Users/andreaseriksen/Desktop/Project F15/code/data/traning"
outputpath = "/Users/andreaseriksen/Desktop/Project F15/code/data/eval/old/wekaoutput.arff"

mf = MatchFilter({"matchMode": ["CLASSIC"],
	                          "matchType": ["MATCHED_GAME"],
	                          "queueType": ["RANKED_SOLO_5x5", "RANKED_PREMADE_5x5", "NORMAL_5x5_BLIND", "NORMAL_5x5_DRAFT"],
	                          "participants->*->timeline->xpPerMinDeltas->*": ["!0"]})

	

feature_creator = FeatureCreator()
team_feature_types = [FeatureType.BLUE_TEAM_SINGLES, FeatureType.RED_TEAM_SINGLES]
feature_creator.set_feature_types(team_feature_types)

wc = WekaConverter(outputpath)

def parsePoint(line): 
	try: 
		match = json.loads(line)
		if mf.passes(match):
			feature_creator.set_match(match)
			#print feature_creator.current_match_features, feature_creator.label
			wc.add(feature_creator.current_match_features, feature_creator.label)
		print "ADDING"
	except:
		print "EXCEPTING"
	return line
			
	
sc = SparkContext("local", "Simple App")
data = sc.textFile(','.join(glob.glob('/Users/andreaseriksen/Desktop/Project F15/code/data/traning/*.txt')))
parsedData = data.map(lambda line: parsePoint(line))
parsedData.count()
wc.set_feature_names(feature_creator.get_all_feature_names())
wc.printlines()
wc.write()
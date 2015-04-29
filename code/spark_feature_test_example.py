from sparkfeaturetest import SparkFeatureTest
from pyspark import SparkContext
import json
from featurecreator.featurecreator import FeatureType
from prediction.matchfilter import MatchFilter
from pyspark.mllib.classification import LogisticRegressionWithSGD

team = [FeatureType.BLUE_TEAM_SINGLES,FeatureType.RED_TEAM_SINGLES]
cross = [FeatureType.CROSS_TEAM_PAIRS]
combo = [FeatureType.BLUE_TEAM_PAIRS, FeatureType.RED_TEAM_PAIRS]
rank = [FeatureType.BEST_RANK]
spells = [FeatureType.SPELL_CHAMPION_COMBO]
lane = [FeatureType.LANE_CHAMPION_COMBO]
  

team_combo = team+combo
team_combo_cross = team+cross+combo
team_crossteam = team+cross
team_best_rank = team+rank
best_rank_team_spell_champion = team+combo+cross+rank+spells+lane

team_spell_champion = team+spells 
 
mf = MatchFilter({"matchMode": ["CLASSIC"],
	                          "matchType": ["MATCHED_GAME"],
	                          "queueType": ["RANKED_SOLO_5x5", "RANKED_PREMADE_5x5", "NORMAL_5x5_BLIND", "NORMAL_5x5_DRAFT", 
	                          "GROUP_FINDER_5x5"],
	                          "participants->*->timeline->xpPerMinDeltas->*": ["!0"]})

	

outputpath = "/home/hduser/share/fis/json"
inputpath = 'hdfs://node1:9000/segmentaa.json'


sc = SparkContext("spark://node1:7077", 'alt')


def __matchfilter__(line):
	try: 
		json_object = json.loads(line)
		if mf.passes(json_object):
			return True
	except:
		return False
	return False


data = sc.textFile(inputpath)

training_data, eval_data = data.filter(lambda line: __matchfilter__(line)).randomSplit([0.7, 0.3], 1)
data.unpersist()
sft = SparkFeatureTest(outputpath, inputpath)


# sft.run("lane", lane,LogisticRegressionWithSGD,training_data, eval_data)
sft.run("team_crossteam", team_crossteam,LogisticRegressionWithSGD,training_data, eval_data)
# sft.run("team_best_rank", team_best_rank,LogisticRegressionWithSGD,training_data, eval_data)
# sft.run("best_rank_team_spell_champion", best_rank_team_spell_champion,LogisticRegressionWithSGD,training_data, eval_data)

sft.run("team", team,LogisticRegressionWithSGD,training_data, eval_data)
sft.run("combo", combo,LogisticRegressionWithSGD,training_data, eval_data)










from sparkfeaturetest import SparkFeatureTest
from pyspark import SparkContext
from featurecreator.featurecreator import FeatureType
from prediction.matchfilter import MatchFilter

team_features = [FeatureType.BLUE_TEAM_SINGLES, FeatureType.RED_TEAM_SINGLES]
combo_features = [FeatureType.BLUE_TEAM_PAIRS, FeatureType.RED_TEAM_PAIRS]
team_combo = [FeatureType.BLUE_TEAM_SINGLES, FeatureType.RED_TEAM_SINGLES, FeatureType.BLUE_TEAM_PAIRS, FeatureType.RED_TEAM_PAIRS]
team_combo_cross = [FeatureType.BLUE_TEAM_SINGLES, FeatureType.RED_TEAM_SINGLES, FeatureType.BLUE_TEAM_PAIRS, FeatureType.RED_TEAM_PAIRS, FeatureType.CROSS_TEAM_PAIRS]
team_crossteam = [FeatureType.BLUE_TEAM_SINGLES, FeatureType.RED_TEAM_SINGLES, FeatureType.CROSS_TEAM_PAIRS]

spell_champion = [FeatureType.SPELL_CHAMPION_COMBO]
team_spell_champion = spell_champion + team_combo_cross
best_rank = [FeatureType.BEST_RANK]
team_best_rank = best_rank + team_features
best_rank_team_spell_champion = best_rank + team_spell_champion



mf = MatchFilter({"matchMode": ["CLASSIC"],
	                          "matchType": ["MATCHED_GAME"],
	                          "queueType": ["RANKED_SOLO_5x5", "RANKED_PREMADE_5x5", "NORMAL_5x5_BLIND", "NORMAL_5x5_DRAFT"],
	                          "participants->*->timeline->xpPerMinDeltas->*": ["!0"]})

	
outputpath = "/home/hduser/share/D802f15/code/test/"
inputpath = 'hdfs://node1:9000/*.json'

sc = SparkContext("spark://node1:7077")

sft = SparkFeatureTest(outputpath, inputpath, mf)

sft.run("single_team", team_features, sc)
sft.run("combos", combo_features, sc)
sft.run("teams_combos", team_combo, sc)
sft.run("team_combo_cross", team_combo_cross, sc)
sft.run("team_crossteam", team_crossteam, sc)

sft.run("spell_champion", spell_champion, sc)
sft.run("team_spell_champion", team_spell_champion, sc)
sft.run("best_rank", best_rank, sc)
sft.run("team_best_rank", team_best_rank, sc)
sft.run("best_rank_team_spell_champion", best_rank_team_spell_champion, sc)


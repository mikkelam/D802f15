import glob
from prediction.features import *
from prediction.trainer import Trainer
from prediction.wordcount import Wordcount
from pyspark.mllib.classification import LogisticRegressionWithSGD
from prediction.matchfilter import MatchFilter
from prediction.wordcount import Wordcount



mf = MatchFilter({})
# mf = MatchFilter({"matchMode": ["CLASSIC"],
#                          "matchType": ["MATCHED_GAME"],
#                          "queueType": ["RANKED_SOLO_5x5", "RANKED_PREMADE_5x5", "NORMAL_5x5_BLIND", "NORMAL_5x5_DRAFT"],
#                          "participants->*->highestAchievedSeasonTier": ["MASTER", "CHALLENGER", "DIAMOND", "PLATINUM"] ,
#                          "participants->*->timeline->xpPerMinDeltas->*": ["!0"]})
#wordcount = Wordcount('hdfs://node1:9000/user/hduser/*.txt', mf, sample=1, local=False)
#wordcount.wordcount()


trainer = Trainer(LogisticRegressionWithSGD, 'hdfs://node1:9000/*.json', mf, team_composition, sample=0.01, local=False)
trainer.train()

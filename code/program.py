import glob
from prediction.features import *
from prediction.trainer import Trainer
from pyspark.mllib.classification import LogisticRegressionWithLBFGS
from prediction.matchfilter import MatchFilter



mf = MatchFilter({})
# mf = MatchFilter({"matchMode": ["CLASSIC"],
#                          "matchType": ["MATCHED_GAME"],
#                          "queueType": ["RANKED_SOLO_5x5", "RANKED_PREMADE_5x5", "NORMAL_5x5_BLIND", "NORMAL_5x5_DRAFT"],
#                          "participants->*->highestAchievedSeasonTier": ["MASTER", "CHALLENGER", "DIAMOND", "PLATINUM"] ,
#                          "participants->*->timeline->xpPerMinDeltas->*": ["!0"]})

trainer = Trainer(LogisticRegressionWithLBFGS, 'data.txt', mf, red_team, blue_team, sample=0.1, local=True)
trainer.train()

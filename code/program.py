import glob
from prediction.features import *
from prediction.trainer import Trainer
from prediction.wordcount import Wordcount
from pyspark.mllib.classification import LogisticRegressionWithLBFGS
from prediction.matchfilter import MatchFilter
from prediction.wordcount import Wordcount



mf = MatchFilter({})
# mf = MatchFilter({"matchMode": ["CLASSIC"],
#                          "matchType": ["MATCHED_GAME"],
#                          "queueType": ["RANKED_SOLO_5x5", "RANKED_PREMADE_5x5", "NORMAL_5x5_BLIND", "NORMAL_5x5_DRAFT"],
#                          "participants->*->highestAchievedSeasonTier": ["MASTER", "CHALLENGER", "DIAMOND", "PLATINUM"] ,
#                          "participants->*->timeline->xpPerMinDeltas->*": ["!0"]})

wordcount = Wordcount('data.txt', mf, sample=0.1, local=True)
wordcount.wordcount()


#trainer = Trainer(LogisticRegressionWithLBFGS, 'data.txt', mf, winning_team, losing_team, sample=0.1, local=True)
#trainer.train()

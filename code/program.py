import glob
from prediction.features import *
from prediction.trainer import Trainer
from pyspark.mllib.classification import LogisticRegressionWithLBFGS
from prediction.matchfilter import MatchFilter



mf = MatchFilter({})

trainer = Trainer(LogisticRegressionWithLBFGS, 'region-euw-start-1971865781-size-1000.txt', mf, two_gram,local=True)
trainer.train()

import glob
from prediction.features import team_composition
from prediction.trainer import Trainer
from pyspark.mllib.classification import LogisticRegressionWithLBFGS
from prediction.utility.matchfilter import MatchFilter



mf = MatchFilter()

trainer = Trainer(LogisticRegressionWithLBFGS, 'region-euw-start-1971865781-size-1000.txt', mf, team_composition)
trainer.train()
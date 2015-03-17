import glob
from prediction.features import team_composition
from prediction.trainer import Trainer
from pyspark.mllib.classification import LogisticRegressionWithLBFGS
from prediction.matchfilter import MatchFilter



mf = MatchFilter()

trainer = Trainer(LogisticRegressionWithLBFGS, 'hdfs://node1:9000/user/hduser/mined-data/*', mf, team_composition,local=False)
trainer.train()

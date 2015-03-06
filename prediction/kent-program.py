# Now we are ready to import Spark Modules
import os
import sys
os.environ['SPARK_HOME']="C:\spark-1.2.14"
sys.path.append("C:\spark-1.2.1\python")
from linearregression.hero_team_win import hero_team_win
from pyspark import SparkContext
import glob
					#hdfs://node1:9000/user/hduser/*.txt // local
sc = SparkContext("hdfs://node1:9000/user/hduser/*.txt", "Linear Regression Basic", 
					pyFiles=[r'C:\Users\Kent\Desktop\D802f15\python\matchfilter\matchfilter.py',
							 r'C:\Users\Kent\Desktop\D802f15\python\utility\utility.py'])
data = sc.textFile(','.join(glob.glob(r'C:\Users\Kent\Desktop\D802f15\LoLMiner\LoLMiner\bin\mined-data\region-euw-start-1971860775-size-1000.txt')))  #"data.txt")

hero_team_win(data)
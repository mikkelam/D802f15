# Now we are ready to import Spark Modules
import sys
import os
from operator import add
os.environ['SPARK_HOME']="C:/spark-1.2.1-bin-hadoop2.4"
os.environ['HADOOP_HOME']="C:/spark-1.2.1-bin-hadoop2.4"
sys.path.append("C:/spark-1.2.1-bin-hadoop2.4/python")
sys.path.append("C:/spark-1.2.1-bin-hadoop2.4/python/build")
try:
    from pyspark import SparkContext
    from pyspark import SparkConf
    print ("Successfully imported Spark Modules")
except ImportError as e:
    print ("Error importing Spark Modules", e)
    sys.exit(1)

from linearregression.hero_team_win import hero_team_win
import glob
conf=SparkConf()
conf.setMaster("local")
conf.setAppName("spark_wc")
sc = SparkContext(conf=conf)

data = sc.textFile(r"C:\Users\Kent\Desktop\D802f15\LoLMiner\LoLMiner\bin\mined-data\region-euw-start-1971860775-size-1000.txt")
hero_team_win(data)
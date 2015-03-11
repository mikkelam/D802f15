from linearregression.hero_team_win import hero_team_win
from pyspark import SparkContext
import glob
					
sc = SparkContext("spark://node1:7077")

data = sc.textFile('hdfs://node1:9000/user/hduser/*.txt')  #"data.txt")
hero_team_win(data)

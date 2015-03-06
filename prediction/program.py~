from linearregression.hero_team_win import hero_team_win
from pyspark import SparkContext
import glob
					#hdfs://node1:9000/user/hduser/*.txt // local
sc = SparkContext("local", "Linear Regression Basic", 
					pyFiles=['/Users/wireless_dk/D802f15/python/matchfilter/matchfilter.py', 
							 '/Users/wireless_dk/D802f15/python/utility/utility.py'])

data = sc.textFile(','.join(glob.glob('../LoLMiner/LoLMiner/data/*.txt')))  #"data.txt")
hero_team_win(data)
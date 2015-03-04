from linearregression.hero_team_win import hero_team_win
from pyspark import SparkContext
import glob

sc = SparkContext("local", "Linear Regression Basic", 
					pyFiles=['/Users/wireless_dk/D802f15/python/matchfilter/matchfilter.py', 
							 '/Users/wireless_dk/D802f15/python/utility/utility.py'])
data = sc.textFile(','.join(glob.glob('../LoLMiner/LoLMiner/src/mined-data/region-euw-start-1971603524-size-1000.txt')))  #"data.txt")

hero_team_win(data)
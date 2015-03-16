import glob
from pyspark import SparkContext
from pyspark import SparkConf
from linearregression.hero_team_win import hero_team_win





sc = SparkContext("local", "SimpleApp")
data = sc.textFile('region-euw-start-1971866781-size-1000.txt')  #"data.txt")

hero_team_win(data)
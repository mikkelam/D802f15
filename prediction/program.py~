from linearregression.hero_team_win import hero_team_win
from linearregression.first_dragon_win import first_dragon_win

from pyspark import SparkContext
import glob
					#hdfs://node1:9000/user/hduser/*.txt // local
sc = SparkContext("local", "Linear Regression Basic", 
					pyFiles=[
							'linearregression/first_dragon_win.py',
							'linearregression/hero_team_win.py',
							'matchfilter/matchfilter.py', 
							'utility/utility.py'])

data = sc.textFile(','.join(glob.glob('../LoLMiner/LoLMiner/data/*.txt')))  #"data.txt")
#hero_team_win(data)

first_dragon_win(data)

import json
import glob 
import sys
from pyspark import SparkContext


def json_filter(line):
	try:
		json_object = json.loads(line)
	except:
		print "false json"
		return (0, 0)
	match_id = json_object["matchId"]
	return (match_id, 1)
	
def duplicate_filter(match):
	print match
	return True
		
sc = SparkContext("spark://node1:7077")
data = sc.textFile('hdfs://node1:9000/user/hduser/mined-data/*')


filtered_data = data.filter(lambda line: json_filter(line))

result = filtered_data.map(lambda line: json_filter(line)).reduceByKey(lambda a, b: a+b)
duplicates = result.filter(lambda (a, b): b > 1)
#number_of_lines = filtered_data.count()
print duplicates.collect()


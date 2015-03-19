from pyspark import SparkContext
import json
class Wordcount:
	"""docstring for Trainer"""
	def __init__(self, data, match_filter, split=[0.7,0.3], seed=1, sample=1, local=True):
		self.match_filter = match_filter
		self.split = split
		self.seed = seed
		self.data = data
		self.local = local
		self.sample = sample
		
	def __filter(self,line):
		#load the json scheme, if the json is not valid, an exception is thrown.
		try:
			json_object = json.loads(line)
		except ValueError, exJson:
			print "json object is not valid"
			return False
		return self.match_filter.passes(json_object)

	def wordcount(self):
		#json_data = map.(load json sample_data)

		if self.local:
		  sc = SparkContext("local", "SimpleApp")
		else:
		  sc = SparkContext("spark://node1:7077")
		data = sc.textFile(self.data)

		linecount = data.count()

		print "LineCounter: ", linecount





from pyspark import SparkContext
import json
class Trainer:
	"""docstring for Trainer"""
	def __init__(self, model, data, match_filter, parse_point, split=[0.7,0.3], seed=1,local=True):
		self.model = model
		self.match_filter = match_filter
		self.parse_point = parse_point
		self.split = split
		self.seed = seed
		self.data = data
		self.local = local
		
	def __filter(self,line):
		#load the json scheme, if the json is not valid, an exception is thrown.
		try:
			json_object = json.loads(line)
		except ValueError, exJson:
			print "json object is not valid"
			return False
		return self.match_filter.passes(json_object)

	def train(self):
		#sample_data = self.data.sample(False,0.1,1)
		#json_data = map.(load json sample_data)

		if self.local:
			sc = SparkContext("local", "SimpleApp")
		else:
		  sc = SparkContext("spark://7077")
		data = sc.textFile(self.data)


		filtered_data = data.filter(self.__filter)

		train_data, eval_data = filtered_data.randomSplit(self.split, self.seed)

		#train the model
		parsed_train_data = train_data.map(self.parse_point)
		trained_model = self.model.train(parsed_train_data)
		
		# Evaluating the model on evaluate data
		parsed_eval_data = eval_data.map(self.parse_point)
		prediction = parsed_eval_data.map(lambda p: (p.label,  trained_model.predict(p.features)))
		eval_err = prediction.filter(lambda (v, p): v != p).count() / float(parsed_eval_data.count())
		
		# Evaluating the model on train data
		prediction = parsed_train_data.map(lambda p: (p.label,  trained_model.predict(p.features)))
		train_err = prediction.filter(lambda (v, p): v != p).count() / float(parsed_train_data.count())


		print "Training Error on Evaluation Data:", eval_err
		print "Training Error on Train Data:", train_err










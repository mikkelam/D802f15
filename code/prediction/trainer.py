from pyspark import SparkContext
import json
class Trainer:
	"""docstring for Trainer"""
	def __init__(self, model, data, match_filter, parse_point1, parse_point2=False, split=[0.7,0.3], seed=1, sample=1, local=True):
		self.model = model
		self.match_filter = match_filter
		self.parse_point1 = parse_point1
		self.parse_point2 = parse_point2
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

	def train(self):
		#json_data = map.(load json sample_data)

		if self.local:
		  sc = SparkContext("local", "SimpleApp")
		else:
		  sc = SparkContext("spark://node1:7077")
		data = sc.textFile(self.data)

		sample_data = data.sample(False, self.sample, self.seed)

		filtered_data = sample_data.filter(self.__filter)

		train_data, eval_data = filtered_data.randomSplit(self.split, self.seed)

		#train the model
		if self.parse_point2 != False:
			parsed_train_data = sc.union([train_data.map(self.parse_point1), train_data.map(self.parse_point2)])
		else:
			parsed_train_data = train_data.map(self.parse_point1)
		trained_model = self.model.train(parsed_train_data)
		
		# Evaluating the model on evaluate data
		if self.parse_point2 != False:
			parsed_eval_data = sc.union([eval_data.map(self.parse_point1), eval_data.map(self.parse_point2)])
		else:
			parsed_eval_data = eval_data.map(self.parse_point1)
		
		prediction = parsed_eval_data.map(lambda p: (p.label,  trained_model.predict(p.features)))
		eval_err = prediction.filter(lambda (v, p): v != p).count() / float(parsed_eval_data.count())
		
		# Evaluating the model on train data
		prediction = parsed_train_data.map(lambda p: (p.label,  trained_model.predict(p.features)))
		train_err = prediction.filter(lambda (v, p): v != p).count() / float(parsed_train_data.count())


		print "Training Error on Evaluation Data:", eval_err
		print "Training Error on Train Data:", train_err







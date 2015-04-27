import json
import os
import glob 
import pickle
import time


from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import SparseVector
from featurecreator.featurecreator import FeatureType, FeatureCreator
from pyspark import SparkContext


class SparkFeatureTest:	
	def __init__(self, outputpath, inputpath, matchfilter):
		self.outputpath = outputpath
		self.inputpath = inputpath
		self.matchfilter = matchfilter
		
		
	def __matchfilter__(self, line):
		try: 
			json_object = json.loads(line)
			if self.matchfilter.passes(json_object):
				return True
			#print self.matchfilter.last_discard_reason
		except:
			return False
		return False
		
		
	def __parsePoint__(self, line):
		match = json.loads(line)
		self.feature_creator.set_match(match)
		
		#Sets the value of all present features to 1 
		total_features = self.feature_creator.number_of_features
		features = {}
		for feature in self.feature_creator.current_match_features:
			features[feature] = 1 
		label = 0.0
		if self.feature_creator.label:
			label = 1.0 
		return LabeledPoint(label, SparseVector(total_features, features)) 
		
		
	def __evaluate__(self, model, parsedData, dataname, file):
		# Test count and test error count. 
		count = parsedData.count()
		# Evaluating the model on train data
		prediction = parsedData.map(lambda p: (p.label,  model.predict(p.features)))
		error = prediction.filter(lambda (v, p): v != p).count()
		
		#Write the results to the file provided from run 
		file.write(dataname + " count: " + str(count) + "\n")
		file.write(dataname + " prediction error: " + str(error)+"\n")
		file.write(dataname + " prediction error %: " + str(error/float(count))+"\n")
		
	def __save_model__(self, model, testname):
		pickle.dump(model, open(self.outputpath + testname +"model.p","wb"))
		


	def run(self, testname, testfeatures, sparkcontext, samples,Model,training_size, local=True):
		if local:
			data = sparkcontext.textFile(','.join(glob.glob(self.inputpath)))
		else:
			data = sparkcontext.textFile(self.inputpath)

		self.feature_creator = FeatureCreator()
		self.feature_creator.set_feature_types(testfeatures)

		traning_set, eval_data1 = data.filter(lambda line: self.__matchfilter__(line)).randomSplit([0.7, 0.3], 1)
		parsedEval_1 = eval_data1.map(lambda line: self.__parsePoint__(line))
		for i in range(0, samples):
			print training_size
			traning_data, _ = traning_set.randomSplit([training_size, 1.0-training_size], 1)
			
			#Maps all data to parsePoints 
			parsedData = traning_data.map(lambda line: self.__parsePoint__(line))

			# Build the model
			model = Model.train(parsedData)
		
			self.__save_model__(model, testname+str(training_size))
			#Evalueates the traning and saves all results
			file = open(self.outputpath + testname + str(training_size) + ".txt",'w')
		
			self.__evaluate__(model, parsedData, "train", file)
			self.__evaluate__(model, parsedEval_1, "eval", file)
			file.close()
			training_size = training_size - 1.0/float(samples)
		


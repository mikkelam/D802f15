import json
import os
import glob 
import pickle

from pyspark.mllib.classification import LogisticRegressionWithSGD
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
		except:
			return False
		return False
		
		
	def __parsePoint__(self, line, features):
		#Generates the features of the game
		feature_creator = FeatureCreator()
		match = json.loads(line)
		feature_creator.set_match(match)
		for feature in features:
			feature_creator.make_features(feature)
		#feature_creator.make_features(FeatureType.RED_TEAM_SINGLES)
		
		#Sets the value of all present features to 1 
		features = {}
		for feature in feature_creator.sparse_feature_list:
			features[feature] = 1 
		return LabeledPoint(int(feature_creator.label), SparseVector(feature_creator.feature_count, features)) 
		
		
	def __evaluate__(self, model, parsedData, dataname, file):
		# Test count and test error count. 
		count = parsedData.count()
		# Evaluating the model on train data
		prediction = parsedData.map(lambda p: (p.label,  model.predict(p.features)))
		error = prediction.filter(lambda (v, p): v != p).count()
		
		#Write the results to the file provided from run 
		file.write(dataname + " count: " + str(count) + "\n")
		file.write(dataname + " prediction error: " + str(error)+"\n")
		
	def __save_model__(self, model, testname):
		pickle.dump(model, open(self.outputpath + testname +"model.p","wb"))
		
	
	
	def run(self, testname, testfeatures, sparkcontext):
		data = sparkcontext.textFile(','.join(glob.glob(self.inputpath + '*.txt')))

		traning_data, eval_data1, eval_data2, eval_data3 = data.filter(lambda line: self.__matchfilter__(line)).randomSplit([0.7, 0.1, 0.1, 0.1], 1)

		#Maps all data to parsePoints 
		parsedData = traning_data.map(lambda line: self.__parsePoint__(line, testfeatures))
		parsedEval_1 = eval_data1.map(lambda line: self.__parsePoint__(line, testfeatures))
		parsedEval_2 = eval_data2.map(lambda line: self.__parsePoint__(line, testfeatures))
		parsedEval_3 = eval_data3.map(lambda line: self.__parsePoint__(line, testfeatures))

		# Build the model
		#model = LogisticRegressionWithSGD.train(parsedData)
		model = pickle.load(open(self.outputpath + testname +"model.p","rb"))
		self.__save_model__(model, testname)
		#Evalueates the traning and saves all results
		file = open(self.outputpath + testname + ".txt",'w')
		
		self.__evaluate__(model, parsedData, "test", file)
		self.__evaluate__(model, parsedEval_1, "eval1", file)
		self.__evaluate__(model, parsedEval_2, "eval2", file)
		self.__evaluate__(model, parsedEval_3, "eval3", file)
		
		file.close()
		
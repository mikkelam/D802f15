import json
import os
import glob 
import pickle
import time
import operator



from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import SparseVector
from featurecreator.featurecreator import FeatureType, FeatureCreator
from pyspark import SparkContext


class SparkFeatureTest:	
	def __init__(self, outputpath, inputpath):
		self.outputpath = outputpath
		self.inputpath = inputpath
		self.timestamp = time.time()
		
	def __parsePoint(self, line):
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
		
		
	def __evaluate(self, model, parsedData, dataname, file):	
		count = parsedData.count()
		prediction = parsedData.map(lambda p: (p.label,  model.predict(p.features)))
		error = prediction.filter(lambda (v, p): v != p).count()
		
		#Write the results to the file provided from run 
		file.write(dataname + " count: " + str(count) + "\n")
		file.write(dataname + " prediction error: " + str(error)+"\n")
		file.write(dataname + " prediction error %: " + str(error/float(count))+"\n")
		file.write(dataname + " prediction error %: " + str(error/float(count))+"\n")


	def __pprint_weights(self, file, model):
		file.write('\n')
		featureweights = {}
		for idx,feature in enumerate(self.feature_creator.get_all_feature_names()):
			featureweights[feature] = model.weights[idx]

		for feature,weight in sorted(featureweights.items(), key=operator.itemgetter(1)):
   			file.write('%s: %s\n' % (feature, weight))


	def __save_model(self, model, testname):
		pickle.dump(model, open(self.outputpath + testname +"model.p","wb"))
		


	def run(self, testname, testfeatures,Model, training_data,eval_data):
		self.feature_creator = FeatureCreator()
		self.feature_creator.set_feature_types(testfeatures)

		parsed_train = training_data.map(lambda line: self.__parsePoint(line))
		parsed_eval = eval_data.map(lambda line: self.__parsePoint(line))
		
		model = Model.train(parsed_train)
		self.__save_model(model, testname)

		file = open(self.outputpath + testname + ".txt",'w')
	
		self.__evaluate(model, parsed_train, "train", file)
		self.__evaluate(model, parsed_eval, "eval", file)
		file.write("\ntimestamp: %s\n" % (time.time()-self.timestamp))

		self.__pprint_weights(file, model)
		file.close()
		parsed_train
		
		


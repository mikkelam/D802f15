import glob
import csv
from prediction.matchfilter import MatchFilter
from pyspark import SparkContext
from pyspark.mllib.classification import LogisticRegressionWithSGD
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import SparseVector

def parsePoint(line):
	A = [i for i in line.strip().split(",")]
	features = [int(i) for i in A[:len(A)-1]]
	if A[-1:][0] == 'True':
		print "true"
		label = 1.0
	else:
		print "false"
		label = 0.0
	feats = {}
	i = 0
	for j in features:
		if j == 1:
			feats[i] = 1
		i = i + 1
	#print A[-1:][0]
	return LabeledPoint(label, SparseVector(len(features), feats)) 
	

outputpath = "/Users/andreaseriksen/Desktop/Project F15/code/data/eval/"
sc = SparkContext("local", "Simple App")
data = sc.textFile(','.join(glob.glob('/Users/andreaseriksen/Desktop/Project F15/code/data/traning/*.csv')))

traning_data, eval_data = data.randomSplit([0.66, 0.34], 1)
parsedData = traning_data.map(parsePoint)
# Build the model
model = LogisticRegressionWithSGD.train(parsedData)
# Evaluating the model on evaluation data
eval_parsedData = eval_data.map(parsePoint)
labelsAndPreds = eval_parsedData.map(lambda p: (p.label, model.predict(p.features)))
trainErr = labelsAndPreds.filter(lambda (v, p): v != p).count()
eval_count = eval_parsedData.count()
test_count = parsedData.count()

f = open(outputpath + 'weka_sparktest_sparse.txt', 'w')
#print float(eval_parsedData.count())
f.write("Training Error = " + str(trainErr))
f.write("\n Eval = " + str(eval_count))
f.write("\n Test = " + str(test_count))
f.close()
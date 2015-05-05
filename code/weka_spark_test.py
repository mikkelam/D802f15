import glob
import csv
from prediction.matchfilter import MatchFilter
from pyspark import SparkContext
from pyspark.mllib.classification import LogisticRegressionWithSGD, SVMWithSGD
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import SparseVector

def parsePoint(line):
	line = line.replace("{", "")
	line = line.replace("}", "")
	A = [i for i in line.strip().split(",")]
	features = [i for i in A[:len(A)-1]]
	print A[-1:][0].split(" ")[2]
	if A[-1:][0].split(" ")[2] == 'True':
		print "true"
		label = 1.0
	else:
		print "false"
		label = 0.0
	feats = {}

	for feature in features:
		feats[int(feature.split(" ")[1])] = 1
		#print i
		
	return LabeledPoint(label, SparseVector(40000, feats)) 
	
def attributefilter(line):
	return line.startswith("{")

outputpath = "/Users/andreaseriksen/Desktop/Project F15/code/data/eval/"
sc = SparkContext("local", "Simple App")
data = sc.textFile(','.join(glob.glob('/Users/andreaseriksen/Desktop/Project F15/code/data/traning/*.arff')))

traning_data, eval_data = data.filter(lambda line: attributefilter(line)).randomSplit([0.66, 0.34], 1)
parsedData = traning_data.map(parsePoint)
# Build the model
model = LogisticRegressionWithSGD.train(parsedData)
# Evaluating the model on evaluation data
eval_parsedData = eval_data.map(parsePoint)
labelsAndPreds = eval_parsedData.map(lambda p: (p.label, model.predict(p.features)))
trainErr = labelsAndPreds.filter(lambda (v, p): v != p).count()
eval_count = eval_parsedData.count()
test_count = parsedData.count()

f = open(outputpath + 'weka_sparktest_sparsesvm.txt', 'w')
#print float(eval_parsedData.count())
f.write("Training Error = " + str(trainErr))
f.write("\n Eval = " + str(eval_count))
f.write("\n Test = " + str(test_count))
f.close()
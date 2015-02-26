from pyspark.mllib.classification import LogisticRegressionWithSGD
from pyspark.mllib.regression import LabeledPoint
from numpy import array
from pyspark import SparkContext
import json
import glob
from utility.utility import champion_index
from matchfilter.matchfilter import MatchFilter

# Load and parse the data
def parse_point(line):
	
	#load the json scheme, if the json is not valid, an exception is thrown.
	try:
		json_object = json.loads(line)
	except ValueError, ex_mathias:
		print "json object is not valid"
		return

	#filter the line, if the content is not relevant
	mf = MatchFilter()
	if not mf.passes(json_object):
		return 

	featureList = [0] * 247 # a list of zeros. index 0 is the label/class, followed by the featurelist
	for p in json_object[ "participants" ]:
		champIndex = 1 # must start with a label
		champIndex += champion_index(p[ "championId" ]) #add 1, as index 0 is the label, not a feature
		if p[ "teamId" ] == 200:
			champIndex += 123 # first 123 is team blue, following 123 is team red
		featureList[champIndex] = 1
	if json_object["participants"][0]["stats"]["winner"] == "true":
		featureList[0] = 1
	return LabeledPoint(featureList[0], featureList[1:]) #LbabeledPoint is imported

def hero_team_win():
	sc = SparkContext("local", "Simple App")
	data = sc.textFile(','.join(glob.glob('../LoLMiner/LoLMiner/src/mined-data/region-euw-start-1971603524-size-1000.txt')))  #"data.txt")
	parsedData = data.map(parse_point)
	model = LogisticRegressionWithSGD.train(parsedData)

	# Evaluating the model on training data
	labelsAndPreds = parsedData.map(lambda p: (p.label,  model.predict(p.features)))
	trainErr = labelsAndPreds.filter(lambda (v, p): v != p).count() / float(parsedData.count())
	print("lines of json: " + str(parsedData.count()))
	print("Training Error = " + str(trainErr))


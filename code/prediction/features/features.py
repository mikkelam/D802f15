from pyspark.mllib.regression import LabeledPoint
from numpy import array


def __champion_index(championId):
  #parms:  champion ID INT
  #return: champion index INT
  #there is no order in the champ Id's, this function returns a useful index for all the heroes
  championList = [266, 103, 84, 12, 32, 34, 1, 22, 268, 53, 63, 201, 51, 69, 31, 42, 122, 131, 36, 119, 60, 28, 81, 9, 114, 105, 3, 41, 86, 150, 79, 104, 120, 74, 39, 40, 59, 24, 126, 222, 429, 43, 30, 38, 55, 10, 85, 121, 96, 7, 64, 89, 127, 236, 117, 99, 54, 90, 57, 11, 21, 82, 25, 267, 75, 111, 76, 56, 20, 2, 61, 80, 78, 133, 33, 421, 58, 107, 92, 68, 13, 113, 35, 98, 102, 27, 14, 15, 72, 37, 16, 50, 134, 91, 44, 17, 412, 18, 48, 23, 4, 29, 77, 6, 110, 67, 45, 161, 254, 112, 8, 106, 19, 62, 101, 5, 157, 83, 154, 238, 115, 26, 143]
  return championList.index(championId)


def team_composition(line):
  #load the json scheme, if the json is not valid, an exception is thrown.
  try:
    json_object = json.loads(line)
  except ValueError, nonvalidjson:
    print "json object is not valid"

  featureList = [0] * 247 # a list of zeros. index 0 is the label/class, followed by the featurelist
  for p in json_object[ "participants" ]:
    champIndex = 1 # index 0 must be the label
    champIndex += __champion_index(p[ "championId" ])
    if p[ "teamId" ] == 200:
      champIndex += 123 # first 123 is team blue, following 123 is team red
    featureList[champIndex] = 1
  if json_object["participants"][0]["stats"]["winner"] == True:
    featureList[0] = 1
  return LabeledPoint(featureList[0], featureList[1:]) #LbabeledPoint is imported



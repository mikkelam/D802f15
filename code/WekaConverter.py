class WekaConverter:
	def __init__(self, total_features, relation="Lol",  path="", mode="w"):
		self.mode = mode
		self.path = path
		self.relation = relation
		self.total_features = total_features
		self.arff_data = ""
		self.file = open(path, mode)
		
	def add(self, feature_list, label):
		self.arff_data += "{"
		for feature in feature_list:
			self.arff_data += "%d 1, " %(feature) 
		self.arff_data += "%d %r}\n" %(self.total_features, label) 
			
	def write(self):
		header = "@RELATION %s\n" % self.relation
		for i in range(0, self.total_features):
			header += "@ATTRIBUTE %d {0, 1}\n" %i
		header += "@ATTRIBUTE %d {False, True}\n@DATA\n" %(i+1)
		self.file.write(header + self.arff_data)
		self.file.close() 

		
wc = WekaConverter(10, path="/Users/andreaseriksen/Desktop/Project F15/code/data/subset/10000Games.csv")
wc.add([1, 3, 5, 6], True)
wc.add([2, 3, 5, 8], False)
wc.write()
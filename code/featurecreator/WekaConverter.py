class WekaConverter:
    def __init__(self, path, relation_name="Lol"):
        self.path = path
        self.relation_name = relation_name
        self.lines = []

    def add(self, feature_list, label):
        self.lines.append([feature_list, label])

    def write(self):
        with open(self.path, "w") as file:
            # write header
            header = "@RELATION %s\n" % self.relation_name
            for name in self.feature_names:
                header += "@ATTRIBUTE " + name + " {0, 1}\n"
            header += "@ATTRIBUTE BLUE-WINS {False, True}\n"
            header += "@DATA\n"
            file.write(header)

            #write data
            for line in self.lines:
                current_line_str = "{"
                features = line[0]
                label = line[1]
                features.sort()
                for feature in features:
                    current_line_str += "%d 1, " %(feature)
                current_line_str += "%d %r}\n" %(len(self.feature_names), label)
                file.write(current_line_str)

    def set_feature_names(self, feature_names):
        self.feature_names = feature_names
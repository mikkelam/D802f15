from sparsefeaturelist import SparseFeatureList

class FeatureType:
    BLUE_TEAM_SINGLES = 1,
    RED_TEAM_SINGLES = 2,
    CROSS_TEAM_PAIRS = 3,
    BLUE_TEAM_PAIRS = 4,
    RED_TEAM_PAIRS = 5,
    FIRST_BLOOD = 6,
    FIRST_DRAGON = 7,
    FIRST_BARON = 8,
    FIRST_INHIBITOR = 9,
    FIRST_TOWER = 10,
    AVG_RANK = 11

class FeatureCreator:
    champion_ids = [266, 103, 84, 12, 32, 34, 1, 22, 268, 53, 63, 201, 51, 69, 31, 42, 122, 131, 36, 119, 60, 28, 81, 9, 114, 105, 3, 41, 86, 150, 79, 104, 120, 74, 39, 40, 59, 24, 126, 222, 429, 43, 30, 38, 55, 10, 85, 121, 96, 7, 64, 89, 127, 236, 117, 99, 54, 90, 57, 11, 21, 82, 25, 267, 75, 111, 76, 56, 20, 2, 61, 80, 78, 133, 33, 421, 58, 107, 92, 68, 13, 113, 35, 98, 102, 27, 14, 15, 72, 37, 16, 50, 134, 91, 44, 17, 412, 18, 48, 23, 4, 29, 77, 6, 110, 67, 45, 161, 254, 112, 8, 106, 19, 62, 101, 5, 157, 83, 154, 238, 115, 26, 143]
    champion_count = len(champion_ids)

    def set_match(self, json_object):
        self.match = json_object
        self.sparse_feature_list = []
        self.label = json_object["teams"][0]["winner"]
        self.feature_count = 0
        self.blue_team = self.__map_champion_ids(True)
        self.red_team = self.__map_champion_ids(False)

    def __map_champion_ids(self, team_blue):
        #Champions IDs from LOL match files are scattered, so map them to a nice clean range from 0 to n.
        ids = []
        for participant in self.match["participants"]:
            if (participant["teamId"] == 100 and team_blue) or (participant["teamId"] == 200 and not team_blue):
                ids.append(FeatureCreator.champion_ids.index(participant["championId"]))
        return ids

    def make_features(self, feature_type):
        function_to_invoke = {
            FeatureType.BLUE_TEAM_SINGLES: lambda: self.__make_single_team(self.blue_team),
            FeatureType.RED_TEAM_SINGLES: lambda: self.__make_single_team(self.red_team),
            FeatureType.BLUE_TEAM_PAIRS: lambda: self.__make_single_team_pairs(self.blue_team),
            FeatureType.RED_TEAM_PAIRS: lambda: self.__make_single_team_pairs(self.red_team),
            FeatureType.CROSS_TEAM_PAIRS: lambda: self.__make_cross_team_pairs(self.red_team, self.blue_team),
			FeatureType.FIRST_BLOOD: lambda: self.__first_something("Blood"),
            FeatureType.FIRST_DRAGON: lambda: self.__first_something("Dragon"),
            FeatureType.FIRST_BARON: lambda: self.__first_something("Baron"),
            FeatureType.FIRST_TOWER: lambda: self.__first_something("Tower"),
            FeatureType.FIRST_INHIBITOR: lambda: self.__first_something("Inhibitor"),
            FeatureType.AVG_RANK: lambda: self.__avg_rank()
        }
        sparse_features = function_to_invoke[feature_type]() #invoke the function that generates features
        for id in sparse_features.sparse_feature_list:
            self.sparse_feature_list.append(id + self.feature_count)
        self.feature_count += sparse_features.feature_count

    def __make_single_team(self, champion_list):
        feature_type_count = len(FeatureCreator.champion_ids)
        feature_ids = []
        for id in champion_list:
            feature_ids.append(id)
        return SparseFeatureList(feature_ids, feature_type_count)

    def __make_cross_team_pairs(self, champion_list1, champion_list2):
        # makes features representing 2-combinations, except pairs (x, x) of two equal values
        feature_type_count = pow(len(self.champion_ids), 2)
        feature_ids = []

        # See our article's description of X3 features for understanding the formula below:
        m = FeatureCreator.champion_count
        for c1 in champion_list1:
            for c2 in champion_list2:
                id = c1*m+c2
                feature_ids.append(id)

        return SparseFeatureList(feature_ids, feature_type_count)

    def __make_single_team_pairs(self, champion_list):
        feature_type_count = (FeatureCreator.champion_count * (FeatureCreator.champion_count - 1)) / 2
        feature_ids = []

        # See our article's description of X2 features for understanding the formula below:
        m = len(self.champion_ids)
        for c1 in champion_list:
            for c2 in champion_list:
                if c1 < c2:
                    id = c1*(2*m-3-c1)//2+c2-1
                    feature_ids.append(id)

        return SparseFeatureList(feature_ids, feature_type_count)

     
    def __avg_rank(self):
        feature_type_count = 1
        ranks = ['BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'DIAMOND', 'MASTER', 'CHALLENGER']

        feature_ids = []
        t1,t2 = 0,0
        t1sum,t2sum = 0,0
        for idx, p in enumerate(json_object["participants"]):
            if p['highestAchievedSeasonTier'] == 'UNRANKED':
                continue
            rank = ranks.index(p['highestAchievedSeasonTier'])
            if p["teamId"] == 200:
                t1+= 1
                t1sum += rank
            else: # team 2
                t2+= 1
                t2sum += rank

        if t1 > 0 and t2 > 0:
            feature_ids.append(int((t2sum/t2) < (t1sum/t1)))

        return SparseFeatureList(feature_ids, feature_type_count)


    def __first_something(self, first_something):
	    feature_type_count = 3
	    feature_value = [2] #noone got first blood
	    if self.match["teams"][0]["first"+first_something]: #blue team got first something
	        feature_value = [0]
	    elif self.match["teams"][1]["first"+first_something]: #red team got first something
	        feature_value = [1]
	    return SparseFeatureList(feature_value, feature_type_count)

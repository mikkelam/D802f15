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
    champion_names = {"266":	"Aatrox", "103":	"Ahri", "84":	"Akali", "12":	"Alistar", "32":	"Amumu", "34":	"Anivia", "1":	"Annie", "22":	"Ashe", "268":	"Azir", "432":	"Bard", "53":	"Blitzcrank", "63":	"Brand", "201":	"Braum", "51":	"Caitlyn", "69":	"Cassiopeia", "31":	"ChoGath", "42":	"Corki", "122":	"Darius", "131":	"Diana", "36":	"DrMundo", "119":	"Draven", "60":	"Elise", "28":	"Evelynn", "81":	"Ezreal", "9":	"Fiddlesticks", "114":	"Fiora", "105":	"Fizz", "3":	"Galio", "41":	"Gangplank", "86":	"Garen", "150":	"Gnar", "79":	"Gragas", "104":	"Graves", "120":	"Hecarim", "74":	"Heimerdinger", "39":	"Irelia", "40":	"Janna", "59":	"JarvanIV", "24":	"Jax", "126":	"Jayce", "222":	"Jinx", "429":	"Kalista", "43":	"Karma", "30":	"Karthus", "38":	"Kassadin", "55":	"Katarina", "10":	"Kayle", "85":	"Kennen", "121":	"KhaZix", "96":	"KogMaw", "7":	"LeBlanc", "64":	"LeSin", "89":	"Leona", "127":	"Lissandra", "236":	"Lucian", "117":	"Lulu", "99":	"Lux", "54":	"Malphite", "90":	"Malzahar", "57":	"Maokai", "11":	"MasterYi", "21":	"MissFortune", "82":	"Mordekaiser", "25":	"Morgana", "267":	"Nami", "75":	"Nasus", "111":	"Nautilus", "76":	"Nidalee", "56":	"Nocturne", "20":	"Nunu", "2":	"Olaf", "61":	"Orianna", "80":	"Pantheon", "78":	"Poppy", "133":	"Quinn", "33":	"Rammus", "421":	"RekSai", "58":	"Renekton", "107":	"Rengar", "92":	"Riven", "68":	"Rumble", "13":	"Ryze", "113":	"Sejuani", "35":	"Shaco", "98":	"Shen", "102":	"Shyvana", "27":	"Singed", "14":	"Sion", "15":	"Sivir", "72":	"Skarner", "37":	"Sona", "16":	"Soraka", "50":	"Swain", "134":	"Syndra", "91":	"Talon", "44":	"Taric", "17":	"Teemo", "412":	"Thresh", "18":	"Tristana", "48":	"Trundle", "23":	"Tryndamere", "4":	"TwistedFate", "29":	"Twitch", "77":	"Udyr", "6":	"Urgot", "110":	"Varus", "67":	"Vayne", "45":	"Veigar", "161":	"VelKoz", "254":	"Vi", "112":	"Viktor", "8":	"Vladimir", "106":	"Volibear", "19":	"Warwick", "62":	"Wukong", "101":	"Xerath", "5":	"XinZhao", "157":	"Yasuo", "83":	"Yorick", "154":	"Zac", "238":	"Zed", "115":	"Ziggs", "26":	"Zilean", "143":	"Zyra"}
    champion_count = len(champion_ids)
    feature_type_size = {
            FeatureType.BLUE_TEAM_SINGLES: champion_count,
            FeatureType.RED_TEAM_SINGLES: champion_count,
            FeatureType.BLUE_TEAM_PAIRS: champion_count * (champion_count - 1),
            FeatureType.RED_TEAM_PAIRS: champion_count * (champion_count - 1),
            FeatureType.CROSS_TEAM_PAIRS: champion_count * champion_count,
            FeatureType.FIRST_BLOOD: 3,
            FeatureType.FIRST_DRAGON: 3,
            FeatureType.FIRST_BARON: 3,
            FeatureType.FIRST_TOWER: 3,
            FeatureType.FIRST_INHIBITOR: 3,
            FeatureType.AVG_RANK: 2
    }

    def __init__(self):
        self.feature_to_index = dict()
        self.feature_creator_functions = {
            FeatureType.BLUE_TEAM_SINGLES: lambda: self.__make_single_team_champions(self.blue_team, "BLUE"),
            FeatureType.RED_TEAM_SINGLES: lambda: self.__make_single_team_champions(self.red_team, "RED"),
            FeatureType.BLUE_TEAM_PAIRS: lambda: self.__make_single_team_pairs(self.blue_team, "BLUE"),
            FeatureType.RED_TEAM_PAIRS: lambda: self.__make_single_team_pairs(self.red_team, "RED"),
            FeatureType.CROSS_TEAM_PAIRS: lambda: self.__make_cross_team_pairs(self.red_team, self.blue_team),
            FeatureType.FIRST_BLOOD: lambda: self.__first_something("Blood"),
            FeatureType.FIRST_DRAGON: lambda: self.__first_something("Dragon"),
            FeatureType.FIRST_BARON: lambda: self.__first_something("Baron"),
            FeatureType.FIRST_TOWER: lambda: self.__first_something("Tower"),
            FeatureType.FIRST_INHIBITOR: lambda: self.__first_something("Inhibitor"),
            FeatureType.AVG_RANK: lambda: self.__avg_rank()
        }

    def set_feature_types(self, feature_types):
        """
        Sets the feature types created by the FeatureCreator, and calculates the number of possible features
        :param feature_types:
        :return:
        """
        self.feature_types = feature_types
        self.number_of_features = 0
        for feature_type in feature_types:
            self.number_of_features += FeatureCreator.feature_type_size[feature_type]

    def set_match(self, json_object):
        self.match = json_object
        self.current_match_features = []
        self.label = json_object["teams"][0]["winner"]
        self.blue_team = self.__map_champion_ids(True)
        self.red_team = self.__map_champion_ids(False)
        for feature_type in self.feature_types:
            self.feature_creator_functions[feature_type]() # invoke the feature creating function

    def __map_champion_ids(self, team_blue):
        """
        Gets the mapped champions ids from team blue or team red.
        Since LOL use very scattered champion ids, we map them to a nice clean range from 0 to n.
        :param team_blue: True to get the blue team champion ids, False to get the red team champion ids.
        :return List of champion ids:
        """
        ids = []
        for participant in self.match["participants"]:
            if (participant["teamId"] == 100 and team_blue) or (participant["teamId"] == 200 and not team_blue):
                ids.append(FeatureCreator.champion_ids.index(participant["championId"]))
        return ids

    def get_champion_name(index):
        lol_champion_index = str(FeatureCreator.champion_ids[index])
        return FeatureCreator.champion_names[lol_champion_index]

    def get_all_feature_names(self):
        return sorted(self.feature_to_index, key=self.feature_to_index.get)

    def __add_feature(self, name):
        # if it is the first time we see a feature with this name, we add it to our dictionary
        if name not in self.feature_to_index:
            self.feature_to_index[name] = len(self.feature_to_index)

        # add feature name to features of current match
        self.current_match_features.append(self.feature_to_index[name])

    def __make_single_team_champions(self, champion_list, team_name):
        for id in champion_list:
            feature_name = FeatureCreator.get_champion_name(id) + "-" + team_name
            self.__add_feature(feature_name)

    def __make_cross_team_pairs(self, champion_list1, champion_list2):
        # makes features representing 2-combinations, except pairs (x, x) of two equal values
        feature_type_count = pow(FeatureCreator.champion_count, 2)
        feature_ids = []

        # See our article's description of X3 features for understanding the formula below:
        m = self.champion_count
        for c1 in champion_list1:
            for c2 in champion_list2:
                c1_name = FeatureCreator.get_champion_name(c1)
                c2_name = FeatureCreator.get_champion_name(c2)
                feature_name = c1_name + "-VS-" + c2_name
                self.__add_feature(feature_name)

    def __make_single_team_pairs(self, champion_list, team_name):
        feature_type_count = (FeatureCreator.champion_count * (FeatureCreator.champion_count - 1)) / 2
        feature_ids = []

        # See our article's description of X2 features for understanding the formula below:
        m = FeatureCreator.champion_count
        for c1 in champion_list:
            for c2 in champion_list:
                if c1 < c2:
                    c1_name = FeatureCreator.get_champion_name(c1)
                    c2_name = FeatureCreator.get_champion_name(c2)
                    feature_name = c1_name + "&" + c2_name + "-" + team_name
                    self.__add_feature(feature_name)

    def __avg_rank(self):
        feature_type_count = 1
        ranks = ['BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'DIAMOND', 'MASTER', 'CHALLENGER']

        feature_ids = []
        t1,t2 = 0,0
        t1sum,t2sum = 0,0
        for idx, p in enumerate(self.match["participants"]):
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
            feature_name = "AVR-RANK-" + str(int((t2sum/t2) < (t1sum/t1)))
            self.__add_feature(feature_name)

    def __first_something(self, first_something):
        if self.match["teams"][0]["first"+first_something]: #blue team got first something
            feature_name = "FIRST" + first_something + "-" + "BLUE"
        elif self.match["teams"][1]["first"+first_something]: #red team got first something
            feature_name = "FIRST" + first_something + "-" + "RED"
        else:
            feature_name = "FIRST" + first_something + "-" + "NONE"
        self.__add_feature(feature_name)



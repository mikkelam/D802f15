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
    BEST_RANK = 11,
    AVG_RANK = 12,
    PATCH_VERSION = 13,
    SPELL_CHAMPION_COMBO = 14,
    LANE_CHAMPION_COMBO = 15



class FeatureCreator:
    champion_names = {432: "Bard", 266:	"Aatrox", 103:	"Ahri", 84:	"Akali", 12:	"Alistar", 32:	"Amumu", 34:	"Anivia", 1:	"Annie", 22:	"Ashe", 268:	"Azir", 432:	"Bard", 53:	"Blitzcrank", 63:	"Brand", 201:	"Braum", 51:	"Caitlyn", 69:	"Cassiopeia", 31:	"ChoGath", 42:	"Corki", 122:	"Darius", 131:	"Diana", 36:	"DrMundo", 119:	"Draven", 60:	"Elise", 28:	"Evelynn", 81:	"Ezreal", 9:	"Fiddlesticks", 114:	"Fiora", 105:	"Fizz", 3:	"Galio", 41:	"Gangplank", 86:	"Garen", 150:	"Gnar", 79:	"Gragas", 104:	"Graves", 120:	"Hecarim", 74:	"Heimerdinger", 39:	"Irelia", 40:	"Janna", 59:	"JarvanIV", 24:	"Jax", 126:	"Jayce", 222:	"Jinx", 429:	"Kalista", 43:	"Karma", 30:	"Karthus", 38:	"Kassadin", 55:	"Katarina", 10:	"Kayle", 85:	"Kennen", 121:	"KhaZix", 96:	"KogMaw", 7:	"LeBlanc", 64:	"LeSin", 89:	"Leona", 127:	"Lissandra", 236:	"Lucian", 117:	"Lulu", 99:	"Lux", 54:	"Malphite", 90:	"Malzahar", 57:	"Maokai", 11:	"MasterYi", 21:	"MissFortune", 82:	"Mordekaiser", 25:	"Morgana", 267:	"Nami", 75:	"Nasus", 111:	"Nautilus", 76:	"Nidalee", 56:	"Nocturne", 20:	"Nunu", 2:	"Olaf", 61:	"Orianna", 80:	"Pantheon", 78:	"Poppy", 133:	"Quinn", 33:	"Rammus", 421:	"RekSai", 58:	"Renekton", 107:	"Rengar", 92:	"Riven", 68:	"Rumble", 13:	"Ryze", 113:	"Sejuani", 35:	"Shaco", 98:	"Shen", 102:	"Shyvana", 27:	"Singed", 14:	"Sion", 15:	"Sivir", 72:	"Skarner", 37:	"Sona", 16:	"Soraka", 50:	"Swain", 134:	"Syndra", 91:	"Talon", 44:	"Taric", 17:	"Teemo", 412:	"Thresh", 18:	"Tristana", 48:	"Trundle", 23:	"Tryndamere", 4:	"TwistedFate", 29:	"Twitch", 77:	"Udyr", 6:	"Urgot", 110:	"Varus", 67:	"Vayne", 45:	"Veigar", 161:	"VelKoz", 254:	"Vi", 112:	"Viktor", 8:	"Vladimir", 106:	"Volibear", 19:	"Warwick", 62:	"Wukong", 101:	"Xerath", 5:	"XinZhao", 157:	"Yasuo", 83:	"Yorick", 154:	"Zac", 238:	"Zed", 115:	"Ziggs", 26:	"Zilean", 143:	"Zyra"}
    champion_count = len(champion_names)
    summoner_spells = {1:'Cleanse', 2:'Clairvoyance', 3:'Exhaust', 4:'Flash', 6:'Ghost', 7:'Heal', 10:'Unknown', 11:'Smite', 12:'Teleport', 13:'Clarity', 14:'Ignite',17:'Garrison', 21:'Barrier',30:'To the King!',31:'SummonerPoroThrow'}
    lanes = ['TOP', 'MIDDLE', 'JUNGLE', 'BOTTOM']
    ranks = ["UNRANKED", "BRONZE", "SILVER", "GOLD", "PLATINUM", "DIAMOND", "MASTER", "CHALLENGER"]
    patches = ['5.6.0.190']

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
            FeatureType.BEST_RANK: lambda: self.__best_rank(),
            FeatureType.AVG_RANK: lambda: self.__champion_ranks(),
            FeatureType.PATCH_VERSION: lambda: self.__patch_version(),
            FeatureType.SPELL_CHAMPION_COMBO: lambda: self.__spell_champion_combo(), 
            FeatureType.LANE_CHAMPION_COMBO: lambda: self.__lane_champion_combo(),
        }
        self.feature_init_functions = {
            FeatureType.BLUE_TEAM_SINGLES: lambda: self.__init_single_team_champions("BLUE"),
            FeatureType.RED_TEAM_SINGLES: lambda: self.__init_single_team_champions("RED"),
            FeatureType.BLUE_TEAM_PAIRS: lambda: self.__init_single_team_pairs("BLUE"),
            FeatureType.RED_TEAM_PAIRS: lambda: self.__init_single_team_pairs("RED"),
            FeatureType.CROSS_TEAM_PAIRS: lambda: self.__init_cross_team_pairs(),
            FeatureType.FIRST_BLOOD: lambda: self.__init_something("Blood"),
            FeatureType.FIRST_DRAGON: lambda: self.__init_something("Dragon"),
            FeatureType.FIRST_BARON: lambda: self.__init_something("Baron"),
            FeatureType.FIRST_TOWER: lambda: self.__init_something("Tower"),
            FeatureType.FIRST_INHIBITOR: lambda: self.__init_something("Inhibitor"),
            FeatureType.BEST_RANK: lambda: self.__init_best_rank(),
            FeatureType.AVG_RANK: lambda: self.__init_champion_ranks(),
            FeatureType.PATCH_VERSION: lambda: self.__init_patch_version(),
            FeatureType.SPELL_CHAMPION_COMBO: lambda: self.__init_spell_champion_combo(),
            FeatureType.LANE_CHAMPION_COMBO: lambda: self.__init_lane_champion_combo(),    
        }

    def set_feature_types(self, feature_types):
        """
        Sets the feature types created by the FeatureCreator, and makes a map from feature names to feature ids
        :param feature_types:
        :return:
        """
        self.feature_types = feature_types

        # init map from feature name to feature id
        self.feature_to_index.clear()
        for feature_type in self.feature_types:
            self.feature_init_functions[feature_type]()
        self.number_of_features = len(self.feature_to_index)

    def set_match(self, json_object):
        self.match = json_object
        self.current_match_features = []
        self.label = json_object["teams"][0]["winner"]
        self.blue_team = self.__get_team_champions(True)
        self.red_team = self.__get_team_champions(False)
        for feature_type in self.feature_types:
            self.feature_creator_functions[feature_type]() # invoke the feature creating function

    def __get_team_champions(self, team_blue):
        ids = []
        for participant in self.match["participants"]:
            if (participant["teamId"] == 100 and team_blue) or (participant["teamId"] == 200 and not team_blue):
                ids.append(participant["championId"])
        return ids

    def get_all_feature_names(self):
        return sorted(self.feature_to_index, key=self.feature_to_index.get)

    def __add_feature(self, name):
        if name not in self.feature_to_index:
            raise Exception("Feature '" + str(name) + "' has not been initialized, so it does not map to any ID.")
        self.current_match_features.append(self.feature_to_index[name])

    def __init_feature(self, name):
        if (name in self.feature_to_index):
            raise Exception("Feature '" + str(name) + "' has already been initialized.")
        self.feature_to_index[name] = len(self.feature_to_index)



    #  BELOW ARE METHODS FOR INITIALIZING A TYPE OF FEATURE FOLLOWED BY METHOD FOR ADDING THAT TYPE OF FEATURE
    #  The initialization step for a type of feature must ensure that all possible features of that type maps
    #  to a unique index.

    def __init_single_team_champions(self, team_name):
        for key in FeatureCreator.champion_names:
            feature_name = FeatureCreator.champion_names[key] + "-" + team_name
            self.__init_feature(feature_name)

    def __make_single_team_champions(self, champion_list, team_name):
        for id in champion_list:
            feature_name = FeatureCreator.champion_names[id] + "-" + team_name
            self.__add_feature(feature_name)

    def __init_cross_team_pairs(self):
        # makes features representing 2-combinations (including the pair of same champion on both teams)
        m = self.champion_count
        for _,c1_name in self.champion_names.items():
            for _,c2_name in self.champion_names.items():

                feature_name = c1_name + "-BLUE-VS-" + c2_name + "-RED"
                self.__init_feature(feature_name)

    def __make_cross_team_pairs(self, champion_list_blue, champion_list_red):
        # makes features representing 2-combinations (including the pair of same champion on both teams)
        m = self.champion_count
        for c1 in champion_list_blue:
            for c2 in champion_list_red:
                c1_name = FeatureCreator.champion_names[c1]
                c2_name = FeatureCreator.champion_names[c2]
                feature_name = c1_name + "-BLUE-VS-" + c2_name + "-RED"
                self.__add_feature(feature_name)

    def __init_single_team_pairs(self, team_name):
        # 2-permutations of champions on a single team
        m = FeatureCreator.champion_count
        for c1_id, c1_name in self.champion_names.items():
            for c2_id, c2_name in self.champion_names.items():
                if c1_id < c2_id:  
                    feature_name = c1_name + "&" + c2_name + "-" + team_name
                    self.__init_feature(feature_name)

    def __make_single_team_pairs(self, champion_list, team_name):
        # 2-permutations of champions on a single team
        m = FeatureCreator.champion_count
        for c1 in champion_list:
            for c2 in champion_list:
                c1_name = FeatureCreator.champion_names[c1]
                c2_name = FeatureCreator.champion_names[c2]
                if c1 < c2:
                    feature_name = c1_name + "&" + c2_name + "-" + team_name
                    self.__add_feature(feature_name)

    def __init_champion_ranks(self):
        for team in ["BLUE", "PURPLE"]:
            for c in ["C1", "C2", "C3", "C4", "C5"]:
                for rank in self.ranks:
                    self.__init_feature("RANK-"+team+"-"+c+"-"+rank)

    def __champion_ranks(self):
        blue_num = 0
        purple_num = 0
        for participant in self.match["participants"]:
            rank = participant["highestAchievedSeasonTier"]
            if participant["teamId"] == 100:
                blue_num += 1
                team = "BLUE"
                num = blue_num
            else:
                purple_num += 1
                team = "PURPLE"
                num = purple_num
            feature_name = "RANK-" + team + "-C" + str(num) + "-" + rank
            self.__add_feature(feature_name)

    def __init_best_rank(self):
        self.__init_feature("BEST-RANK-BLUE")
        self.__init_feature("BEST-RANK-RED")
        self.__init_feature("BEST-RANK-NONE")

    def __best_rank(self):
        feature_type_count = 1
        t1sum,t2sum = 0,0
        for idx, p in enumerate(self.match["participants"]):
            if p['highestAchievedSeasonTier'] == 'UNRANKED':
                continue
            rank = self.ranks.index(p['highestAchievedSeasonTier'])
            if p["teamId"] == 100:
                t1sum += rank
            else: # team 2
                t2sum += rank
        best_rank = "BLUE" if t1sum > t2sum else ("RED" if t2sum > t1sum else "NONE")
        feature_name = "BEST-RANK-" + best_rank
        self.__add_feature(feature_name)

    def __init_first_something(self, first_something):
        self.__init_feature("FIRST" + first_something + "-" + "BLUE")
        self.__init_feature("FIRST" + first_something + "-" + "RED")
        self.__init_feature("FIRST" + first_something + "-" + "NONE")

    def __first_something(self, first_something):
        if self.match["teams"][0]["first"+first_something]: #blue team got first something
            feature_name = "FIRST" + first_something + "-" + "BLUE"
        elif self.match["teams"][1]["first"+first_something]: #red team got first something
            feature_name = "FIRST" + first_something + "-" + "RED"
        else:
            feature_name = "FIRST" + first_something + "-" + "NONE"
        self.__add_feature(feature_name)


    def __init_patch_version(self):
        for p in self.patches:
            self.__init_feature('PATCH-' + p)
    def __patch_version(self):
        return self.__add_feature("PATCH-" + self.match['matchVersion'])


    def __init_spell_champion_combo(self):
        #team?
        for _,c in FeatureCreator.champion_names.items():
            for id1,spell1 in self.summoner_spells.items():
                for id2,spell2 in self.summoner_spells.items():
                    if id1 > id2:
                        continue
                    feature_name = c + '-S1-' + spell1 + '-S2-' + spell2
                    self.__init_feature(feature_name)
        with open('f', 'w+') as f:
            f.write(str(self.feature_to_index))


    def __spell_champion_combo(self):
        for p in self.match['participants']:
            c = FeatureCreator.champion_names[p['championId']]
            spell_id1 = p['spell1Id']
            spell_id2 = p['spell2Id']
            if spell_id1 > spell_id2:
                spell_id1,spell_id2 = spell_id2, spell_id1
            spell1 = self.summoner_spells[spell_id1]
            spell2 = self.summoner_spells[spell_id2]
            feature_name = c + '-S1-' + spell1 + '-S2-' + spell2
            self.__add_feature(feature_name)

    def __init_lane_champion_combo(self):
        for _,c in FeatureCreator.champion_names.items():
            for lane in self.lanes:
                feature_name = c + '-' + lane
                self.__init_feature(feature_name)


    def __lane_champion_combo(self):
        for p in self.match['participants']:
            c = FeatureCreator.champion_names[p['championId']]
            lane = p['timeline']['lane']
            feature_name = c + '-' + lane
            self.__add_feature(feature_name)
        

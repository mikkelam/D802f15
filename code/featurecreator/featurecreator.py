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
    BEST_RANKED_TEAM = 11,
    PLAYER_RANKS = 12,
    PATCH_VERSION = 13,
    SPELL_CHAMPION_COMBO = 14,
    LANE_CHAMPION_COMBO = 15,
    CHAMPION_RANK = 16,
    CHAMPION_MASTERIES = 17,
    CHAMPION_RUNE = 18,
    CHAMPION_QUEUE = 19

    

class FeatureCreator:
    masteries = {
	4262: "Tenacious", 4311: "Phasewalker", 4244: "Evasive", 4322: "Summoner's Insight", 4242: "Swiftness", 4243: "Reinforced Armor", 4241: "Perseverance ", 4224: "Bladed Armor", 4314: "Scout", 4142: "Warlord", 4343: "Expanded Mind", 4221: "Unyielding", 4222: "Veteran's Scars", 4344: "Inspiration", 4162: "Havoc", 4123: "Mental Force", 4122: "Brute Force", 4121: "Expose Weakness", 4362: "Wanderer", 4141: "Blade Weaving", 4143: "Archmage", 4124: "Feast", 4341: "Scavenger", 4323: "Strength of Spirit", 4214: "Tough Skin", 4312: "Fleet of Foot", 4313: "Meditation", 4211: "Block", 4342: "Wealth", 4213: "Enchanted Armor", 4212: "Recovery", 4251: "Second Wind", 4253: "Runic Blessing", 4252: "Legendary Guardian", 4332: "Runic Affinity", 4333: "Vampirism", 4324: "Alchemist", 4352: "Bandit", 4114: "Butcher", 4112: "Fury", 4113: "Sorcery", 4111: "Double-Edged Sword", 4234: "Resistance", 4233: "Hardiness", 4232: "Juggernaut", 4231: "Oppression", 4353: "Intelligence", 4152: "Devastating Strikes", 4151: "Frenzy", 4334: "Culinary Master", 4154: "Arcane Blade", 4131: "Spell Weaving", 4132: "Martial Mastery", 4133: "Arcane Mastery", 4134: "Executioner", 4144: "Dangerous Game", 4331: "Greed"}
	
    runes = {5173: "Glyph of Cooldown Reduction", 5196: "Seal of Scaling Armor", 5177: "Glyph of Mana", 5176: "Glyph of Scaling Ability Power", 5175: "Glyph of Ability Power", 5174: "Glyph of Scaling Cooldown Reduction", 5418: "Greater Quintessence of Hybrid Penetration", 5179: "Glyph of Mana Regeneration", 5178: "Glyph of Scaling Mana", 5229: "Quintessence of Health Regeneration", 5316: "Greater Seal of Scaling Health", 8014: "Quintessence of the Piercing Screech", 5078: "Lesser Seal of Scaling Health Regeneration", 5359: "Greater Quintessence of Mana", 8019: "Greater Quintessence of the Piercing Present", 5072: "Lesser Seal of Scaling Health", 5073: "Lesser Seal of Armor", 8015: "Quintessence of Bountiful Treats", 5071: "Lesser Seal of Health", 5076: "Lesser Seal of Scaling Magic Resist", 5077: "Lesser Seal of Health Regeneration", 5074: "Lesser Seal of Scaling Armor", 5075: "Lesser Seal of Magic Resist", 5417: "Quintessence of Hybrid Penetration", 5275: "Greater Glyph of Attack Damage", 5208: "Seal of Scaling Mana", 5277: "Greater Glyph of Attack Speed", 5270: "Greater Mark of Scaling Mana", 5271: "Greater Mark of Mana Regeneration", 8003: "Glyph of the Special Stocking", 5273: "Greater Mark of Magic Penetration", 5374: "Greater Quintessence of Energy", 5371: "Greater Glyph of Energy", 5279: "Greater Glyph of Critical Damage", 5373: "Greater Quintessence of Energy Regeneration", 5372: "Greater Glyph of Scaling Energy", 8013: "Quintessence of the Headless Horseman", 5409: "Greater Quintessence of Spell Vamp", 5065: "Lesser Seal of Critical Damage", 5067: "Lesser Seal of Critical Chance", 5061: "Lesser Seal of Attack Damage", 5063: "Lesser Seal of Attack Speed", 5062: "Lesser Seal of Scaling Attack Damage", 5146: "Mark of Scaling Ability Power", 5147: "Mark of Mana", 5145: "Mark of Ability Power", 5143: "Mark of Cooldown Reduction", 5243: "Quintessence of Movement Speed", 5228: "Quintessence of Scaling Magic Resist", 8022: "Greater Quintessence of Sugar Rush", 8020: "Greater Quintessence of the Deadly Wreath", 8021: "Greater Quintessence of Frosty Health", 5413: "Lesser Seal of Percent Health", 5341: "Greater Quintessence of Critical Chance", 5267: "Greater Mark of Ability Power", 5309: "Greater Seal of Critical Damage", 5265: "Greater Mark of Cooldown Reduction", 5259: "Greater Mark of Magic Resist", 5260: "Greater Mark of Scaling Magic Resist", 5300: "Greater Glyph of Scaling Mana", 5301: "Greater Glyph of Mana Regeneration", 5302: "Greater Glyph of Scaling Mana Regeneration", 5303: "Greater Glyph of Magic Penetration", 5305: "Greater Seal of Attack Damage", 5269: "Greater Mark of Mana", 5268: "Greater Mark of Scaling Ability Power", 5411: "Quintessence of Life Steal", 5159: "Glyph of Critical Chance", 5011: "Lesser Mark of Health", 5012: "Lesser Mark of Scaling Health", 5013: "Lesser Mark of Armor", 5015: "Lesser Mark of Magic Resist", 5016: "Lesser Mark of Scaling Magic Resist", 5151: "Mark of Magic Penetration", 5348: "Greater Quintessence of Scaling Armor", 5153: "Glyph of Attack Damage", 5336: "Greater Quintessence of Scaling Attack Damage", 5155: "Glyph of Attack Speed", 5154: "Glyph of Scaling Attack Damage", 5157: "Glyph of Critical Damage", 5349: "Greater Quintessence of Magic Resist", 5339: "Greater Quintessence of Critical Damage", 5306: "Greater Seal of Scaling Attack Damage", 8016: "Quintessence of the Speedy Specter", 5307: "Greater Seal of Attack Speed", 5414: "Seal of Percent Health", 5099: "Lesser Quintessence of Armor Penetration", 5319: "Greater Seal of Magic Resist", 5251: "Greater Mark of Critical Chance", 5256: "Greater Mark of Scaling Health", 5257: "Greater Mark of Armor", 5412: "Greater Quintessence of Life Steal", 5255: "Greater Mark of Health", 5091: "Lesser Quintessence of Attack Damage", 5092: "Lesser Quintessence of Scaling Attack Damage", 5093: "Lesser Quintessence of Attack Speed", 5317: "Greater Seal of Armor", 5095: "Lesser Quintessence of Critical Damage", 5315: "Greater Seal of Health", 5097: "Lesser Quintessence of Critical Chance", 5281: "Greater Glyph of Critical Chance", 8011: "Lesser Glyph of the Challenger", 5410: "Lesser Quintessence of Life Steal", 5003: "Lesser Mark of Attack Speed", 5002: "Lesser Mark of Scaling Attack Damage", 5001: "Lesser Mark of Attack Damage", 5007: "Lesser Mark of Critical Chance", 5005: "Lesser Mark of Critical Damage", 5009: "Lesser Mark of Armor Penetration", 5276: "Greater Glyph of Scaling Attack Damage", 5327: "Greater Seal of Ability Power", 5343: "Greater Quintessence of Armor Penetration", 5325: "Greater Seal of Cooldown Reduction", 5322: "Greater Seal of Scaling Health Regeneration",5129: "Mark of Critical Chance", 5320: "Greater Seal of Scaling Magic Resist", 5321: "Greater Seal of Health Regeneration", 5124: "Mark of Scaling Attack Damage", 5125: "Mark of Attack Speed", 5127: "Mark of Critical Damage", 5121: "Lesser Quintessence of Movement Speed", 5328: "Greater Seal of Scaling Ability Power", 5123: "Mark of Attack Damage", 5401: "Mark of Hybrid Penetration", 5406: "Greater Quintessence of Percent Health", 5405: "Quintessence of Percent Health", 5088: "Lesser Seal of Scaling Mana Regeneration", 5249: "Greater Mark of Critical Damage", 5402: "Greater Mark of Hybrid Penetration", 5298: "Greater Glyph of Scaling Ability Power", 5400: "Lesser Mark of Hybrid Penetration", 5083: "Lesser Seal of Ability Power", 5352: "Greater Quintessence of Scaling Health Regeneration", 5081: "Lesser Seal of Cooldown Reduction", 5246: "Greater Mark of Scaling Attack Damage", 5087: "Lesser Seal of Mana Regeneration", 5086: "Lesser Seal of Scaling Mana", 5085: "Lesser Seal of Mana", 5084: "Lesser Seal of Scaling Ability Power", 5415: "Greater Seal of Percent Health", 8008: "Mark of the Combatant", 5346: "Greater Quintessence of Scaling Health", 8035: "Greater Quintessence of Studio Rumble", 5299: "Greater Glyph of Mana", 5037: "Lesser Glyph of Critical Chance", 5035: "Lesser Glyph of Critical Damage", 5032: "Lesser Glyph of Scaling Attack Damage", 5033: "Lesser Glyph of Attack Speed", 5031: "Lesser Glyph of Attack Damage", 5331: "Greater Seal of Mana Regeneration", 5209: "Seal of Mana Regeneration", 5332: "Greater Seal of Scaling Mana Regeneration", 5335: "Greater Quintessence of Attack Damage", 5337: "Greater Quintessence of Attack Speed", 5138: "Mark of Scaling Magic Resist", 5137: "Mark of Magic Resist", 5135: "Mark of Armor", 5134: "Mark of Scaling Health", 5133: "Mark of Health", 8006: "Lesser Seal of the Stout Snowman", 5131: "Mark of Armor Penetration", 5238: "Quintessence of Scaling Mana", 5239: "Quintessence of Mana Regeneration", 8001: "Mark of the Crippling Candy Cane", 5113: "Lesser Quintessence of Ability Power", 5230: "Quintessence of Scaling Health Regeneration", 5233: "Quintessence of Cooldown Reduction", 5234: "Quintessence of Scaling Cooldown Reduction", 5235: "Quintessence of Ability Power", 5236: "Quintessence of Scaling Ability Power", 5237: "Quintessence of Mana", 8002: "Lesser Mark of the Yuletide Tannenbaum ", 5297: "Greater Glyph of Ability Power", 5253: "Greater Mark of Armor Penetration", 5329: "Greater Seal of Mana", 5408: "Quintessence of Spell Vamp", 5029: "Lesser Mark of Magic Penetration", 5407: "Lesser Quintessence of Spell Vamp", 8017: "Quintessence of the Witches Brew", 5021: "Lesser Mark of Cooldown Reduction", 5023: "Lesser Mark of Ability Power", 5025: "Lesser Mark of Mana", 5024: "Lesser Mark of Scaling Ability Power", 5027: "Lesser Mark of Mana Regeneration", 5026: "Lesser Mark of Scaling Mana", 5108: "Lesser Quintessence of Scaling Health Regeneration", 5404: "Lesser Quintessence of Percent Health", 5102: "Lesser Quintessence of Scaling Health", 5103: "Lesser Quintessence of Armor", 5101: "Lesser Quintessence of Health", 5106: "Lesser Quintessence of Scaling Magic Resist", 5107: "Lesser Quintessence of Health Regeneration", 5104: "Lesser Quintessence of Scaling Armor", 5105: "Lesser Quintessence of Magic Resist", 5183: "Seal of Attack Damage", 5180: "Glyph of Scaling Mana Regeneration", 5181: "Glyph of Magic Penetration", 5187: "Seal of Critical Damage", 5184: "Seal of Scaling Attack Damage", 5185: "Seal of Attack Speed", 5223: "Quintessence of Health", 5221: "Quintessence of Armor Penetration", 5189: "Seal of Critical Chance", 5227: "Quintessence of Magic Resist", 5226: "Quintessence of Scaling Armor", 5225: "Quintessence of Armor", 5224: "Quintessence of Scaling Health", 5245: "Greater Mark of Attack Damage", 8005: "Lesser Glyph of the Gracious Gift", 8012: "Glyph of the Soaring Slalom", 5247: "Greater Mark of Attack Speed", 5213: "Quintessence of Attack Damage", 5115: "Lesser Quintessence of Mana", 5114: "Lesser Quintessence of Scaling Ability Power", 5117: "Lesser Quintessence of Mana Regeneration", 5116: "Lesser Quintessence of Scaling Mana", 5111: "Lesser Quintessence of Cooldown Reduction", 10001: "Razer Mark of Precision", 10002: "Razer Quintessence of Speed", 5112: "Lesser Quintessence of Scaling Cooldown Reduction", 5296: "Greater Glyph of Scaling Cooldown Reduction", 5241: "Quintessence of Magic Penetration", 5295: "Greater Glyph of Cooldown Reduction", 5119: "Lesser Quintessence of Magic Penetration", 5118: "Lesser Quintessence of Scaling Mana Regeneration", 5290: "Greater Glyph of Scaling Magic Resist", 5240: "Quintessence of Scaling Mana Regeneration", 5217: "Quintessence of Critical Damage", 5214: "Quintessence of Scaling Attack Damage", 5215: "Quintessence of Attack Speed", 5058: "Lesser Glyph of Scaling Mana Regeneration", 5059: "Lesser Glyph of Magic Penetration", 5210: "Seal of Scaling Mana Regeneration", 5054: "Lesser Glyph of Scaling Ability Power", 5055: "Lesser Glyph of Mana", 5056: "Lesser Glyph of Scaling Mana", 5057: "Lesser Glyph of Mana Regeneration", 5051: "Lesser Glyph of Cooldown Reduction", 5052: "Lesser Glyph of Scaling Cooldown Reduction", 5053: "Lesser Glyph of Ability Power", 5357: "Greater Quintessence of Ability Power", 5356: "Greater Quintessence of Scaling Cooldown Reduction", 5355: "Greater Quintessence of Cooldown Reduction", 5199: "Seal of Health Regeneration", 5148: "Mark of Scaling Mana", 5351: "Greater Quintessence of Health Regeneration", 5350: "Greater Quintessence of Scaling Magic Resist", 5195: "Seal of Armor", 5194: "Seal of Scaling Health", 5197: "Seal of Magic Resist", 5149: "Mark of Mana Regeneration", 5193: "Seal of Health", 5358: "Greater Quintessence of Scaling Ability Power", 5345: "Greater Quintessence of Health", 5347: "Greater Quintessence of Armor", 5219: "Quintessence of Critical Chance", 5370: "Greater Seal of Scaling Energy Regeneration", 5289: "Greater Glyph of Magic Resist", 5163: "Glyph of Health", 5164: "Glyph of Scaling Health", 5165: "Glyph of Armor", 5167: "Glyph of Magic Resist", 5168: "Glyph of Scaling Magic Resist", 5169: "Glyph of Health Regeneration", 5285: "Greater Glyph of Health", 5416: "Lesser Quintessence of Hybrid Penetration", 5287: "Greater Glyph of Armor", 5286: "Greater Glyph of Scaling Health", 5200: "Seal of Scaling Health Regeneration", 5203: "Seal of Cooldown Reduction", 5318: "Greater Seal of Scaling Armor", 5205: "Seal of Ability Power", 8009: "Lesser Seal of the Medalist", 5207: "Seal of Mana", 5206: "Seal of Scaling Ability Power", 5047: "Lesser Glyph of Health Regeneration", 5046: "Lesser Glyph of Scaling Magic Resist", 5045: "Lesser Glyph of Magic Resist", 8007: "Lesser Mark of Alpine Attack Speed", 5043: "Lesser Glyph of Armor", 5042: "Lesser Glyph of Scaling Health", 5041: "Lesser Glyph of Health", 5198: "Seal of Scaling Magic Resist", 5362: "Greater Quintessence of Scaling Mana Regeneration", 5363: "Greater Quintessence of Magic Penetration", 5360: "Greater Quintessence of Scaling Mana", 5361: "Greater Quintessence of Mana Regeneration", 5366: "Greater Quintessence of Revival", 5367: "Greater Quintessence of Gold", 5365: "Greater Quintessence of Movement Speed", 5368: "Greater Quintessence of Experience", 5369: "Greater Seal of Energy Regeneration", 5291: "Greater Glyph of Health Regeneration", 5330: "Greater Seal of Scaling Mana", 5311: "Greater Seal of Critical Chance", 5403: "Greater Seal of Gold"}
	
	
    champion_names = {432: "Bard", 266:	"Aatrox", 103:	"Ahri", 84:	"Akali", 12:	"Alistar", 32:	"Amumu", 34:	"Anivia", 1:	"Annie", 22:	"Ashe", 268:	"Azir", 432:	"Bard", 53:	"Blitzcrank", 63:	"Brand", 201:	"Braum", 51:	"Caitlyn", 69:	"Cassiopeia", 31:	"ChoGath", 42:	"Corki", 122:	"Darius", 131:	"Diana", 36:	"DrMundo", 119:	"Draven", 60:	"Elise", 28:	"Evelynn", 81:	"Ezreal", 9:	"Fiddlesticks", 114:	"Fiora", 105:	"Fizz", 3:	"Galio", 41:	"Gangplank", 86:	"Garen", 150:	"Gnar", 79:	"Gragas", 104:	"Graves", 120:	"Hecarim", 74:	"Heimerdinger", 39:	"Irelia", 40:	"Janna", 59:	"JarvanIV", 24:	"Jax", 126:	"Jayce", 222:	"Jinx", 429:	"Kalista", 43:	"Karma", 30:	"Karthus", 38:	"Kassadin", 55:	"Katarina", 10:	"Kayle", 85:	"Kennen", 121:	"KhaZix", 96:	"KogMaw", 7:	"LeBlanc", 64:	"LeSin", 89:	"Leona", 127:	"Lissandra", 236:	"Lucian", 117:	"Lulu", 99:	"Lux", 54:	"Malphite", 90:	"Malzahar", 57:	"Maokai", 11:	"MasterYi", 21:	"MissFortune", 82:	"Mordekaiser", 25:	"Morgana", 267:	"Nami", 75:	"Nasus", 111:	"Nautilus", 76:	"Nidalee", 56:	"Nocturne", 20:	"Nunu", 2:	"Olaf", 61:	"Orianna", 80:	"Pantheon", 78:	"Poppy", 133:	"Quinn", 33:	"Rammus", 421:	"RekSai", 58:	"Renekton", 107:	"Rengar", 92:	"Riven", 68:	"Rumble", 13:	"Ryze", 113:	"Sejuani", 35:	"Shaco", 98:	"Shen", 102:	"Shyvana", 27:	"Singed", 14:	"Sion", 15:	"Sivir", 72:	"Skarner", 37:	"Sona", 16:	"Soraka", 50:	"Swain", 134:	"Syndra", 91:	"Talon", 44:	"Taric", 17:	"Teemo", 412:	"Thresh", 18:	"Tristana", 48:	"Trundle", 23:	"Tryndamere", 4:	"TwistedFate", 29:	"Twitch", 77:	"Udyr", 6:	"Urgot", 110:	"Varus", 67:	"Vayne", 45:	"Veigar", 161:	"VelKoz", 254:	"Vi", 112:	"Viktor", 8:	"Vladimir", 106:	"Volibear", 19:	"Warwick", 62:	"Wukong", 101:	"Xerath", 5:	"XinZhao", 157:	"Yasuo", 83:	"Yorick", 154:	"Zac", 238:	"Zed", 115:	"Ziggs", 26:	"Zilean", 143:	"Zyra"}
    champion_count = len(champion_names)

    summoner_spells = {1:'Cleanse', 2:'Clairvoyance', 3:'Exhaust', 4:'Flash', 6:'Ghost', 7:'Heal', 8:'unknown1', 9:'unknown2', 10: 'unknown3', 11:'Smite', 12:'Teleport', 13:'Clarity', 14:'Ignite', 15:'unknown4', 16:'unknown5', 17:'Garrison', 18:'unknown6', 19:'unknown7', 20:'unknown8', 21:'Barrier', 30:'To the King!', 31:'SummonerPoroThrow'}
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
            FeatureType.BEST_RANKED_TEAM: lambda: self.__best_rank(),
            FeatureType.PLAYER_RANKS: lambda: self.__player_ranks(),
            FeatureType.PATCH_VERSION: lambda: self.__patch_version(),
            FeatureType.SPELL_CHAMPION_COMBO: lambda: self.__spell_champion_combo(), 
            FeatureType.LANE_CHAMPION_COMBO: lambda: self.__lane_champion_combo(),
            FeatureType.CHAMPION_RANK: lambda: self.__champion_rank(),
            FeatureType.CHAMPION_MASTERIES: lambda: self.__champion_masteries(),
            FeatureType.CHAMPION_RUNE: lambda: self.__champion_runes(),   
            FeatureType.CHAMPION_QUEUE: lambda: self.__champion_queue(),
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
            FeatureType.BEST_RANKED_TEAM: lambda: self.__init_best_rank(),
            FeatureType.PLAYER_RANKS: lambda: self.__init_player_ranks(),
            FeatureType.PATCH_VERSION: lambda: self.__init_patch_version(),
            FeatureType.SPELL_CHAMPION_COMBO: lambda: self.__init_spell_champion_combo(),
            FeatureType.LANE_CHAMPION_COMBO: lambda: self.__init_lane_champion_combo(),   
            FeatureType.CHAMPION_RANK: lambda: self.__init_champion_rank(),
            FeatureType.CHAMPION_MASTERIES: lambda: self.__init_champion_masteries(),
            FeatureType.CHAMPION_RUNE: lambda: self.__init_champion_runes(),   
            FeatureType.CHAMPION_QUEUE: lambda: self.__init_champion_queue(),
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

    def __init_player_ranks(self):
        for team in ["BLUE", "RED"]:
            for c in ["C1", "C2", "C3", "C4", "C5"]:
                for rank in self.ranks:
                    self.__init_feature("RANK-"+team+"-"+c+"-"+rank)

    def __player_ranks(self):
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
                team = "RED"
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
        for _,c in FeatureCreator.champion_names.items():
            for id1,spell1 in self.summoner_spells.items():
                for id2,spell2 in self.summoner_spells.items():
                    if id1 > id2:
                        continue
                    feature_name_blue = c + '-S1-' + spell1 + '-S2-' + spell2 + '-BLUE'
                    feature_name_red = c + '-S1-' + spell1 + '-S2-' + spell2 + '-RED'
                    self.__init_feature(feature_name_blue)
                    self.__init_feature(feature_name_red)


    def __spell_champion_combo(self):
        for p in self.match['participants']:
            c = FeatureCreator.champion_names[p['championId']]
            if p['teamId'] == 100:
                team_color = "BLUE"
            if p['teamId'] == 200:
                team_color = "RED"
            spell_id1 = p['spell1Id']
            spell_id2 = p['spell2Id']
            if spell_id1 > spell_id2:
                spell_id1,spell_id2 = spell_id2, spell_id1
            spell1 = self.summoner_spells[spell_id1]
            spell2 = self.summoner_spells[spell_id2]
            feature_name = c + '-S1-' + spell1 + '-S2-' + spell2 + '-' + team_color
            self.__add_feature(feature_name)


    def __init_lane_champion_combo(self):
        for _,c in FeatureCreator.champion_names.items():
            for lane in self.lanes:
                feature_name = c + '-' + lane + "-BLUE"
                self.__init_feature(feature_name)
        for _,c in FeatureCreator.champion_names.items():
            for lane in self.lanes:
                feature_name = c + '-' + lane + "-RED"
                self.__init_feature(feature_name)


    def __lane_champion_combo(self):
        for p in self.match['participants']:
            c = FeatureCreator.champion_names[p['championId']]
            if p['teamId'] == 100:
                team_color = "BLUE"
            if p['teamId'] == 200:
                team_color = "RED"
            lane = p['timeline']['lane']
            feature_name = c + '-' + lane + "-" + team_color
            self.__add_feature(feature_name)


    def __init_champion_rank(self):
        ranks = ['UNRANKED', 'BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'DIAMOND', 'MASTER', 'CHALLENGER']
        for _,c in FeatureCreator.champion_names.items():
            for rank in ranks:
                blue_feature_name = c + '-' + rank + "-BLUE"
                red_feature_name = c + '-' + rank + "-RED"
                self.__init_feature(blue_feature_name)
                self.__init_feature(red_feature_name)


    def __champion_rank(self):
        for p in self.match['participants']:
            c = FeatureCreator.champion_names[p['championId']]
            rank = p['highestAchievedSeasonTier']
            if p['teamId'] == 100:
                team_color = "BLUE"
            if p['teamId'] == 200:
                team_color = "RED"
            feature_name = c + '-' + rank + '-' + team_color
            self.__add_feature(feature_name)


    def __init_champion_masteries(self):
        ranges = ["0-5", "6-10", "11-15", "16-20", "21-25", "26-30"]
        for _, c in FeatureCreator.champion_names.items():
	        no_masteries_blue = c + "-NOMASTERIES-BLUE"  
	        no_masteries_red = c + "-NOMASTERIES-RED"  
	        self.__init_feature(no_masteries_blue)
	        self.__init_feature(no_masteries_red)
	        for _, mastery in FeatureCreator.masteries.items():
	            blue_mastery_name = c + "-" + mastery + "-BLUE"
	            red_mastery_name = c + "-" + mastery + "-RED"
	            self.__init_feature(blue_mastery_name)
	            self.__init_feature(red_mastery_name)
	        for range in ranges:
	            blue_feature_name = c + '-masteries-' + range + "-BLUE"
	            red_feature_name = c + '-masteries-' + range + "-RED"
	            self.__init_feature(blue_feature_name)
	            self.__init_feature(red_feature_name)


    def __get_range(self, rank):
        strrange = ""
        if rank in range(0, 6):
            strrange = "0-5"
        if rank in range(6,11):
            strrange = "6-10"
        if rank in range(11, 16):
            strrange = "11-15"
        if rank in range(16, 21):
            strrange = "16-20"
        if rank in range(21,26):
            strrange = "21-25"
        if rank in range(26, 31):
            strrange = "26-30"
        return strrange

    def __champion_masteries(self):
        for p in self.match['participants']:
            c = FeatureCreator.champion_names[p['championId']]
            if p['teamId'] == 100:
                team_color = "BLUE"
            if p['teamId'] == 200:
                team_color = "RED"
            try:
                rank = 0
                for mastery in p["masteries"]:
                    mastery_name = FeatureCreator.masteries[mastery["masteryId"]]
                    rank += int(mastery["rank"])
                    feature_name = c + '-' + mastery_name + '-' + team_color
                    self.__add_feature(feature_name)
                range = self.__get_range(rank)
                feature_rank = c + '-masteries-' + range + "-" + team_color
                self.__add_feature(feature_rank)
            except:
                no_masteries = c + "-NOMASTERIES-" + team_color
                self.__add_feature(no_masteries)
                

    def __init_champion_runes(self):
        ranges = ["0-5", "6-10", "11-15", "16-20", "21-25", "26-30"]
        for _, c in FeatureCreator.champion_names.items():
            no_runes_blue = c + "-NORUNES-BLUE"  
            no_runes_red = c + "-NORUNES-RED"  
            self.__init_feature(no_runes_blue)
            self.__init_feature(no_runes_red)
            for _, rune in FeatureCreator.runes.items():
                blue_rune_name = c + "-" + rune + "-BLUE"
                red_rune_name = c + "-" + rune + "-RED"
                self.__init_feature(blue_rune_name)
                self.__init_feature(red_rune_name)
            for range in ranges:
                blue_feature_name = c + '-runes-' + range + "-BLUE"
                red_feature_name = c + '-runes-' + range + "-RED"
                self.__init_feature(blue_feature_name)
                self.__init_feature(red_feature_name)

    def __champion_runes(self):   
        for p in self.match['participants']:
            c = FeatureCreator.champion_names[p['championId']]
            if p['teamId'] == 100:
                team_color = "BLUE"
            if p['teamId'] == 200:
                team_color = "RED"
            try:
                rank = 0
                for rune in p["runes"]:
                    rune_name = FeatureCreator.runes[rune["runeId"]]
                    rank += int(rune["rank"])
                    feature_name = c + '-' + rune_name + '-' + team_color
                    self.__add_feature(feature_name)
                range = self.__get_range(rank)
                feature_rank = c + '-runes-' + range + "-" + team_color
                self.__add_feature(feature_rank)
            except:
                no_runes = c + "-NORUNES-" + team_color
                self.__add_feature(no_runes)

    def __init_champion_queue(self):
        queues = ["NORMAL_5x5_BLIND", "RANKED_SOLO_5x5", "RANKED_PREMADE_5x5", "NORMAL_5x5_DRAFT", "RANKED_TEAM_5x5",  "GROUP_FINDER_5x5"]
        for _,c in FeatureCreator.champion_names.items():
            for queue in queues:
                blue_feature_name = c + '-' + queue + "-BLUE"
                red_feature_name = c + '-' + queue + "-RED"
                self.__init_feature(blue_feature_name)
                self.__init_feature(red_feature_name)


    def __champion_queue(self):
        queueType = self.match['queueType']
        for p in self.match['participants']:
            c = FeatureCreator.champion_names[p['championId']]
            if p['teamId'] == 100:
                team_color = "BLUE"
            if p['teamId'] == 200:
                team_color = "RED"
            feature_name = c + '-' + queueType + '-' + team_color
            self.__add_feature(feature_name)






  
        

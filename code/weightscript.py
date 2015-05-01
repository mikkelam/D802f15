import pickle
import operator
from featurecreator.featurecreator import FeatureType, FeatureCreator

team = [FeatureType.BLUE_TEAM_SINGLES,FeatureType.RED_TEAM_SINGLES]
cross = [FeatureType.CROSS_TEAM_PAIRS]
combo = [FeatureType.BLUE_TEAM_PAIRS, FeatureType.RED_TEAM_PAIRS]
rank = [FeatureType.BEST_RANK]
spells = [FeatureType.SPELL_CHAMPION_COMBO]
lane = [FeatureType.LANE_CHAMPION_COMBO]

team_combo = team+combo
team_combo_cross = team+cross+combo
team_crossteam = team+cross
team_best_rank = team+rank
best_rank_team_spell_champion = team+combo+cross+rank+spells+lane




fc = FeatureCreator()
fc.set_feature_types(team_crossteam)


def pprint_weights(file, model,fc):
    file.write('\n')
    featureweights = {}
    for idx,feature in enumerate(fc.get_all_feature_names()):
        featureweights[feature] = model.weights[idx]

    for feature,weight in sorted(featureweights.items(), key=operator.itemgetter(1)):
        file.write('%s: %s\n' % (feature, weight))

path = '/Users/mikkel/Documents/models/'
model = pickle.load(open(path + 'jsonteam_crossteammodel.p'))
f = open(path + 'jsonteam_crossteammodel.weights', 'w')
pprint_weights(f,model,fc)





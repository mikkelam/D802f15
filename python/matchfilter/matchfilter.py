import json

class MatchFilter:
    def __init__(self):
        self.last_discard_reason = ''

    def __smart_filter(self, filter, json_object):
        """
        Returns whether a json_object passes a filter.
        #filter: A dictionary of (k, v) pairs, where k is a string and v is a list og values.
        #to pass the filter, the json_object must for each attribute k have a value found in v.
        """
        for key in filter:
                passes = False
                for val in filter[key]:
                    if json_object[key] == val:
                        passes = True
                if not passes:
                    self.last_discard_reason = "Value of '" + key + "' = '" + json_object[key] + "' not found in filter."
                    return False
        return True

    def __passes_participants(self, json_object):
        filter = {
            "highestAchievedSeasonTier": ["MASTER", "CHALLENGER", "DIAMOND", "PLATINUM"]
        }
        return self.__smart_filter(filter, json_object)
        
    def __passes_game_type(self, json_object):
        filter = {
            "matchMode": ["CLASSIC"],
            "matchType": ["MATCHED_GAME"],
            "queueType": ["RANKED_SOLO_5x5", "RANKED_PREMADE_5x5", "NORMAL_5x5_BLIND", "NORMAL_5x5_DRAFT"]
        }
        return self.__smart_filter(filter, json_object)

    def __passes_no_leavers(self, json_object):
        #If any participant has not XP in one of the 10 minute windows, he must have been afk, and we discard the game
        for participant in json_object["participants"]:
            for time_window in participant["timeline"]["xpPerMinDeltas"]:
                if participant["timeline"]["xpPerMinDeltas"][time_window] == 0:
                    self.last_discard_reason = "Participant with id: " + str(participant["participantId"]) +\
                                               " has xpPerMinDeltas = 0 for window " + time_window
                    return False
        return True

    def passes(self, json_object):
        """ Takes a json_object representing a LoL match as input, and returns whether it passes our filter."""
        return self.__passes_game_type(json_object) and self.__passes_no_leavers(json_object) and self.__passes_participants(json_object)
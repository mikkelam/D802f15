import json
import fnmatch
import re

class MatchFilter:
    def __init__(self,
                 filter={}):
        self.last_discard_reason = ''
        self.filter = filter
        self.min_avg_rank = 0

    def set_min_avg_rank(self, val):
        # input: a val between 0 and 1, where
        self.min_avg_rank = val

    def __smart_filter(self, filter, json_object):
        """
        Returns whether a json_object passes a smart-filter.
        Example of a filter:
        {
        a->b->c: [x, y, z],
        f->*->g: [v]
        }
        See __smart_filter_check_path(path, allowed_values, json_object) for specification of how a single filter line works
        """

        for key_value_pair in filter:
            if not self.__smart_filter_check_path(key_value_pair, filter[key_value_pair], json_object):
                return False

        if self.min_avg_rank > 0:
            return self.__passes_min_avr_rank(json_object)
        else:
            return True

    def __passes_min_avr_rank(self, json_object):
        if not "participants" in json_object:
            return False
        sum_ranks = 0
        unranked = 0
        for participant in json_object["participants"]:
            if "highestAchievedSeasonTier" not in participant:
                return False
            else:
                rank = participant["highestAchievedSeasonTier"]
                if rank == "UNRANKED": # treat as bronze
                    unranked += 1
                    continue # treat as mean of all ranked players
                if rank == "BRONZE":
                    continue # treat as 0
                elif rank == "SILVER":
                    sum_ranks += 1
                elif rank == "GOLD":
                    sum_ranks += 2
                elif rank == "PLATINUM":
                    sum_ranks += 3
                elif rank == "DIAMOND":
                    sum_ranks += 4
                elif rank == "MASTER":
                    sum_ranks += 5
                elif rank == "CHALLENGER":
                    sum_ranks += 6
        if unranked > 5: # we don't want to include games with more than half being unranked
            return 0
        avg_of_ranked = sum_ranks / len(json_object["participants"])
        sum_ranks += avg_of_ranked * unranked # treat unranked as mean of all ranked players
        avg_rank = sum_ranks / (len(participant) * 6.0) # normalization
        return avg_rank >= self.min_avg_rank


    def __smart_filter_check_path(self, path, allowed_values, json_object):
        """
        Example: a->b: ["x", "!y"]
        Meaning: Check that json_object[a][b] is either x or not y.
        Example: a->*->b: ["x", "y", "z"]
        Meaning: For all v in json_object[a], v[b] must be either x, y, or z.
        Example: a: ["%x", "y"]
        Meaning: For all v in json_object[a], v must either match the regular expression x, or be a y
        """
        head_and_tail = path.split("->", 1) #"a->b->c->d" becomes ["a", "b->c->d"]
        head = head_and_tail[0]
        if len(head_and_tail) > 1:
            tail = head_and_tail[1]
        else:
            tail = ""

        if head == "*":
            for key in json_object:
                if tail == "":
                    if not self.__smart_filter_check_path(key, allowed_values, json_object):
                        return False
                else:
                    if not self.__smart_filter_check_path(tail, allowed_values, key):
                        return False

            return True
        else:
            if not head in json_object:
                self.last_discard_reason = "Match did not have the key '" + str(head) + "'"
                return False
            elif tail == "":
                for val in allowed_values:
                    if (val[0] == "!"): #First character in a key may be NOT operator
                        if not self.compare_values(json_object[head], val[1:]):
                            return True
                    else:
                        if self.compare_values(json_object[head], val):
                            return True
                self.last_discard_reason = "Value of '" + str(head) + "' was '" + str(json_object[head]) + "' and did not match any of allowed values: " + str(allowed_values)
                return False
            else:
                return self.__smart_filter_check_path(tail, allowed_values, json_object[head])

    def compare_values(self, actual, expected):
        if (expected[0] == "%"): #indicates the rest is a regular expression
            return re.match(expected[1:], actual)
        else:
            return actual == expected

#5[.]3[.]0[.]291
    def passes(self, json_object):
        return self.__smart_filter(self.filter, json_object)

        """ Takes a json_object representing a LoL match as input, and returns whether it passes our filter."""
        #return self.__passes_game_type(json_object) and self.__passes_no_leavers(json_object) and self.__passes_participants(json_object)
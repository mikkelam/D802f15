import json

class MatchFilter:
    def __init__(self):
        self.last_discard_reason = ''

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
        return True

    def __smart_filter_check_path(self, path, allowed_values, json_object):
        """
        Example: a->b: ["x", "!y"]
        Meaning: Check that json_object[a][b] is either x or not y.
        Example: a->*->b: ["x", "y", "z"]
        Meaning: For all v in json_object[a], v[b] must be either x, y, or z.
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
                        if json_object[head] != val[1:]:
                            return True
                    else:
                        if json_object[head] == val:
                            return True
                self.last_discard_reason = "Value of '" + str(head) + "' was '" + str(json_object[head]) + "' and did not match any of allowed values: " + str(allowed_values)
                return False
            else:
                return self.__smart_filter_check_path(tail, allowed_values, json_object[head])

    def passes(self, json_object):
        filter = {
            
        }
        return self.__smart_filter(filter, json_object)

        """ Takes a json_object representing a LoL match as input, and returns whether it passes our filter."""
        #return self.__passes_game_type(json_object) and self.__passes_no_leavers(json_object) and self.__passes_participants(json_object)
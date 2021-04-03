from HypixelAPIWrapper.Util.Exceptions import InvalidAPIKeyError
from HypixelAPIWrapper.Util.HelperFunctions import *
import requests


class Other:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.hypixel.net/"

    def get_template(self, request_type):
        """ a template function used to get the given information completed for a given uuid, and their points """

        if not is_api_key_valid(self.api_key):
            raise InvalidAPIKeyError

        # in the case we dont want to retrieve the info from the cache
        # we request new information
        params = {"key": self.api_key}
        results = requests.get(self.url + request_type, params=params).json()

        # if the query results are available
        if results['success']:

            # remove the column we do not need
            del results['success']
            return results
        return results['cause'] if "cause" in results else None

    def get_booster_list(self):
        return self.get_template("boosters")

    def get_player_counts(self):
        return self.get_template("counts")

    def get_leaderboards(self):
        return self.get_template("leaderboards")

    def get_punishment_statistics(self):
        return self.get_template("punishmentstats")


if __name__ == "__main__":
    h = Other(apikey)
    print(h.get_leaderboards())

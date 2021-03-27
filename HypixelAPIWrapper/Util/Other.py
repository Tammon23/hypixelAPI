from HypixelAPIWrapper.Util.Exceptions import InvalidAPIKeyError
from HypixelAPIWrapper.Util.HelperFunctions import *
import requests


class Other:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.hypixel.net/"
        self.cached_data = {}

    def isDataAlreadyCached(self, _type):
        """ Returns if data is already cached for user """
        return _type in self.cached_data, "No cached results for user available"

    def get_template(self, _type, cache_results=False, return_result_if_cached=False, get_from_cache=False):
        """
        a template function used to get the given information completed for a given uuid, and their points
        :param _type:
        :param get_from_cache:
        :param uuid:
        :param cache_results:
        :param return_result_if_cached:
        :return:
        """

        if not is_api_key_valid(self.api_key):
            raise InvalidAPIKeyError

        # if we want to retrieve the info from the cache
        if get_from_cache:

            # we check if what is there is cached data for achievements
            if self.isDataAlreadyCached(_type):

                # if so, we return that data
                return self.cached_data[_type]
            else:
                return None

        # in the case we dont want to retrieve the info from the cache
        # we request new information
        params = {"key": self.api_key}
        results = requests.get(self.url + _type, params=params).json()

        # if the query results are available
        if results['success']:

            # remove the column we do not need
            del results['success']
            if cache_results:
                self.cached_data[_type] = results
                if not return_result_if_cached:
                    return None
            return results
        return results['cause'] if "cause" in results else None

    def get_booster_list(self, cache_results=False, return_result_if_cached=False, get_from_cache=False):
        return self.get_template("boosters", cache_results, return_result_if_cached, get_from_cache)

    def get_player_counts(self, cache_results=False, return_result_if_cached=False, get_from_cache=False):
        return self.get_template("counts", cache_results, return_result_if_cached, get_from_cache)

    def get_leaderboards(self, cache_results=False, return_result_if_cached=False, get_from_cache=False):
        return self.get_template("leaderboards", cache_results, return_result_if_cached, get_from_cache)

    def get_punishment_statistics(self, cache_results=False, return_result_if_cached=False, get_from_cache=False):
        return self.get_template("punishmentstats", cache_results, return_result_if_cached, get_from_cache)


if __name__ == "__main__":
    h = Other(apikey)
    print(h.get_leaderboards())

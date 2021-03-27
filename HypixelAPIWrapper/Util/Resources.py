from HypixelAPIWrapper.Util.HelperFunctions import *
import requests


class Resources:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.hypixel.net/resources/"
        self.cached_data = None
        self.cached_uuid = None
        self.cached_type = None

    def isDataAlreadyCached(self, uuid, _type):
        """ Returns if data is already cached for user """
        return self.cached_data is not None and self.cached_uuid == uuid and self.cached_type == _type, "No cached results for user available"

    def get_template(self, _type, uuid, cache_results=False, return_result_if_cached=False, get_from_cache=False):
        """
        a template function used to get the given information completed for a given uuid, and their points
        :param _type:
        :param get_from_cache:
        :param uuid:
        :param cache_results:
        :param return_result_if_cached:
        :return:
        """

        # if we want to retrieve the info from the cache
        if get_from_cache:

            # we check if what is there is cached data for achievements
            if self.isDataAlreadyCached(uuid, _type):

                # if so, we return that data
                return self.cached_data
            else:
                return None

        # in the case we dont want to retrieve the info from the cache
        # we request new information
        params = {"uuid": uuid, "key": self.api_key}
        results = requests.get(self.url + _type, params=params).json()

        # if the query results are available
        if results['success']:

            # remove the column we do not need
            del results['success']
            if cache_results:
                self.cached_uuid = uuid
                self.cached_data = results
                self.cached_type = _type
                if not return_result_if_cached:
                    return None
            return results
        return results['cause'] if "cause" in results else None

    def get_achievements(self, uuid, cache_results=False, return_result_if_cached=False, get_from_cache=False):
        return self.get_template("achievements", uuid, cache_results, return_result_if_cached, get_from_cache)

    def get_challenges(self, uuid, cache_results=False, return_result_if_cached=False, get_from_cache=False):
        return self.get_template("challenges", uuid, cache_results, return_result_if_cached, get_from_cache)

    def get_quests(self, uuid, cache_results=False, return_result_if_cached=False, get_from_cache=False):
        return self.get_template("quests", uuid, cache_results, return_result_if_cached, get_from_cache)

    def get_guild_achievements(self, uuid, cache_results=False, return_result_if_cached=False, get_from_cache=False):
        return self.get_template("guilds/achievements", uuid, cache_results, return_result_if_cached, get_from_cache)

    def get_guild_permissions(self, uuid, cache_results=False, return_result_if_cached=False, get_from_cache=False):
        return self.get_template("guilds/permissions", uuid, cache_results, return_result_if_cached, get_from_cache)


if __name__ == "__main__":
    h = Resources(apikey)
    UUID = username_to_uuid("Tammon")
    print(h.get_guild_permissions(UUID))

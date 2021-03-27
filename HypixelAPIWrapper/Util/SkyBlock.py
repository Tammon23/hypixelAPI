from HypixelAPIWrapper.Util.HelperFunctions import *
import requests


class SkyBlock:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.hypixel.net/"
        self.cached_data = None
        self.cached_uuid = None
        self.cached_type = None

    def isDataAlreadyCached(self, uuid, _type):
        """ Returns if data is already cached for user """
        return self.cached_data is not None and self.cached_uuid == uuid and self.cached_type == _type, "No cached results for user available"

    def get_template(self, _type, method_key=None, cache_results=False, return_result_if_cached=False, get_from_cache=False, method="uuid"):
        """
        a template function used to get the given information completed for a given uuid, and their points
        :param _type:
        :param get_from_cache:
        :param method_key:
        :param cache_results:
        :param return_result_if_cached:
        :return:
        """

        # if we want to retrieve the info from the cache
        if get_from_cache:

            # we check if what is there is cached data for achievements
            if self.isDataAlreadyCached(method_key, _type):

                # if so, we return that data
                return self.cached_data
            else:
                return None

        # in the case we dont want to retrieve the info from the cache
        # we request new information
        params = {method: method_key, "key": self.api_key}
        results = requests.get(self.url + _type, params=params).json()

        # if the query results are available
        if results['success']:

            # remove the column we do not need
            del results['success']
            if cache_results:
                self.cached_uuid = method_key
                self.cached_data = results
                self.cached_type = _type
                if not return_result_if_cached:
                    return None
            return results
        return None

    def get_collections(self, uuid, cache_results=False, return_result_if_cached=False, get_from_cache=False):
        return self.get_template("resources/skyblock/collections", uuid, cache_results, return_result_if_cached, get_from_cache)

    def get_skills(self, uuid, cache_results=False, return_result_if_cached=False, get_from_cache=False):
        return self.get_template("resources/skyblock/skills", uuid, cache_results, return_result_if_cached, get_from_cache)

    def get_news(self, cache_results=False, return_result_if_cached=False, get_from_cache=False):
        return self.get_template("skyblock/news", cache_results, return_result_if_cached, get_from_cache)

    def get_auction(self, method_key, method="uuid", cache_results=False, return_result_if_cached=False, get_from_cache=False):
        """
        Gets all auction items of a particular player or profile
        :param method_key: the uuid, player name or profile name of the auctioneer
        :param method: uuid, player, profile
        :param cache_results:
        :param return_result_if_cached:
        :param get_from_cache:
        :return:
        """
        if method != "uuid" and method != "player" and method != "profile":
            raise Exception("Available methods are uuid, player, profile!")
        return self.get_template("skyblock/auction", method_key, cache_results, return_result_if_cached, get_from_cache, method)

    def get_auctions(self, page, cache_results=False, return_result_if_cached=False, get_from_cache=False):
        """
        gets actives auctions
        :param page:
        :param cache_results:
        :param return_result_if_cached:
        :param get_from_cache:
        :return:
        """

        # if we want to retrieve the info from the cache
        if get_from_cache:

            # we check if what is there is cached data for achievements
            if self.isDataAlreadyCached(page, "skyblock/auctions"):

                # if so, we return that data
                return self.cached_data
            else:
                return None

        # in the case we dont want to retrieve the info from the cache
        # we request new information
        params = {"page": page, "key": self.api_key}
        results = requests.get(self.url + "skyblock/auctions", params=params).json()

        # if the query results are available
        if results['success']:

            # remove the column we do not need
            del results['success']
            if cache_results:
                self.cached_uuid = page
                self.cached_data = results
                self.cached_type = "skyblock/auctions"
                if not return_result_if_cached:
                    return None
            return results
        return None

    def get_auctions_ended(self, cache_results=False, return_result_if_cached=False, get_from_cache=False):
        return self.get_template("skyblock/auctions_ended", cache_results, return_result_if_cached, get_from_cache)

    def get_bazaar(self, cache_results=False, return_result_if_cached=False, get_from_cache=False):
        """ Returns the list of products along with their sell summary, buy summary and quick status.
            Product fields:
                buy_summary, sell_summary, quick_status

            buy_summary and sell_summary are the current top 30 orders for each transaction type
                (in-game example: https://imgur.com/SjRONxq)

            quick_status is a computed summary of the live state of the product (used for advanced
                 mode view in the bazaar):

            sellVolume and buyVolume are the sum of item amounts in all orders.
                -sellPrice and buyPrice are the weighted average of the top 2% of orders by volume.
                -movingWeek is the historic transacted volume from last 7d + live state.
                -sellOrders and buyOrders are the count of active orders.

        """
        return self.get_template("skyblock/bazaar", cache_results, return_result_if_cached, get_from_cache)

    def get_profile_by_uuid(self, uuid, cache_results=False, return_result_if_cached=False, get_from_cache=False):
        return self.get_template("skyblock/profile", cache_results, return_result_if_cached, get_from_cache)


if __name__ == "__main__":
    h = SkyBlock(apikey)
    print(h.get_bazaar().keys())

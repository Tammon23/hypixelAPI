from HypixelAPIWrapper.Util.Exceptions import InvalidAPIKeyError
from HypixelAPIWrapper.Util.HelperFunctions import *
import requests


class SkyBlock:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.hypixel.net/"

    def get_template(self, request_type, method_key=None, method="uuid"):
        """ a template function used to get the given information completed for a given uuid, and their point """

        if not is_api_key_valid(self.api_key):
            raise InvalidAPIKeyError

        # Requesting new information
        params = {method: method_key, "key": self.api_key}
        results = requests.get(self.url + request_type, params=params).json()

        # if the query results are available
        if results['success']:
            # remove the column we do not need
            del results['success']
            return results
        return results['cause'] if "cause" in results else None

    def get_collections(self, uuid):
        return self.get_template("resources/skyblock/collections", uuid)

    def get_skills(self, uuid):
        return self.get_template("resources/skyblock/skills", uuid)

    def get_news(self):
        return self.get_template("skyblock/news")

    def get_auction(self, method_key, method="uuid"):
        """ Gets all auction items of a particular player or profile. Availiable methods are uuid, player, profile """

        if method != "uuid" and method != "player" and method != "profile":
            raise Exception("Available methods are uuid, player, profile!")
        return self.get_template("skyblock/auction", method_key, method)

    def get_auctions(self, page):
        """ gets actives auctions """

        if is_api_key_valid(self.api_key):
            raise InvalidAPIKeyError

        # Requesting new information
        params = {"page": page, "key": self.api_key}
        results = requests.get(self.url + "skyblock/auctions", params=params).json()

        # if the query results are available
        if results['success']:

            # remove the column we do not need
            del results['success']
            return results
        return results['cause'] if "cause" in results else None

    def get_auctions_ended(self):
        return self.get_template("skyblock/auctions_ended")

    def get_bazaar(self):
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
        return self.get_template("skyblock/bazaar")

    def get_profile_by_uuid(self, uuid):
        return self.get_template("skyblock/profile", uuid)

    def get_profile_by_player(self, uuid):
        return self.get_template("skyblock/profiles", uuid)


if __name__ == "__main__":
    h = SkyBlock(apikey)
    print(h.get_profile_by_player(username_to_uuid("Tammon")))

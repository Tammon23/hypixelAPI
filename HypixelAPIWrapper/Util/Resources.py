from HypixelAPIWrapper.Util.HelperFunctions import *
import requests


class Resources:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.hypixel.net/resources/"

    def get_template(self, request_type, uuid):
        """ a template function used to get the given information completed for a given uuid, and their points """

        # Requesting new information
        params = {"uuid": uuid, "key": self.api_key}
        results = requests.get(self.url + request_type, params=params).json()

        # if the query results are available
        if results['success']:
            # remove the column we do not need
            del results['success']
            return results
        return results['cause'] if "cause" in results else None

    def get_achievements(self, uuid):
        return self.get_template("achievements", uuid)

    def get_challenges(self, uuid):
        return self.get_template("challenges", uuid)

    def get_quests(self, uuid):
        return self.get_template("quests", uuid)

    def get_guild_achievements(self, uuid):
        return self.get_template("guilds/achievements", uuid)

    def get_guild_permissions(self, uuid):
        return self.get_template("guilds/permissions", uuid)


if __name__ == "__main__":
    h = Resources(apikey)
    UUID = username_to_uuid("Tammon")
    print(h.get_guild_permissions(UUID))

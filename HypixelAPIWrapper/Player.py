from HypixelAPIWrapper.HelperFunctions import *
import requests
import json


class Player:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.hypixel.net/player"

    def get_player_data(self, uuid):
        """
        Gets all the data of a user
        :param uuid:
        :return:
        """
        parmas = {"uuid": uuid, "key": self.api_key}
        r = requests.get(self.url, params=parmas)
        r = json.loads(r.content)
        if r['success']:
            return r['player']
        return None

    def get_firstLogin(self, uuid):
        """
        Gets the first hypixel logon time
        :param uuid:
        :return:
        """
        data = self.get_player_data(uuid)
        if data is not None:
            return self.get_player_data(uuid)['firstLogin']
        return None

    def get_lastLogin(self, uuid):
        """
        Gets player last logon time
        :param uuid: UUID of player
        :return:
        """
        data = self.get_player_data(uuid)
        if data is not None:
            return self.get_player_data(uuid)['lastLogin']
        return None

    def get_achievementsOneTime(self, uuid):
        """
        Gets all the completed one time achievements
        :param uuid:
        :return:
        """
        data = self.get_player_data(uuid)
        if data is not None:
            return self.get_player_data(uuid)['achievementsOneTime']
        return None

    def get_achievements(self, uuid):
        """
        Gets all the progress of tiered achievements
        :param uuid:
        :return:
        """
        data = self.get_player_data(uuid)
        if data is not None:
            return self.get_player_data(uuid)['achievements']
        return None

    def get_stats(self, uuid, gamemode_id=None):
        """
        Gets stats of all games merged
        :param uuid:
        :param gamemode_id:
        :return:
        """
        data = self.get_player_data(uuid)
        if data is not None:
            if gamemode_id is not None:
                return self.get_player_data(uuid)['player']['stats'][gamemode_id]
            return self.get_player_data(uuid)['stats']
        return None

    def get_networkExp(self, uuid):
        """
        Gets current network exp
        :param uuid:
        :return:
        """
        data = self.get_player_data(uuid)
        if data is not None:
            return self.get_player_data(uuid)['networkExp']
        return None

    def get_quests(self, uuid, quest_id=None):
        """
        Gets all completed quests lifetime
        :param uuid:
        :param gamemode_id:
        :return:
        """
        data = self.get_player_data(uuid)
        if data is not None:
            if quest_id is not None:
                return self.get_player_data(uuid)['quests'][quest_id]
            return self.get_player_data(uuid)['quests']
        return None

    def get_eugene(self, uuid):
        """
        Gets the dailyTwoKExp
        :param uuid:
        :return:
        """
        data = self.get_player_data(uuid)
        if data is not None:
            return self.get_player_data(uuid)['eugene']
        return None

    def get_karma(self, uuid):
        """
        Gets the total karma
        :param uuid:
        :return:
        """
        data = self.get_player_data(uuid)
        if data is not None:
            return self.get_player_data(uuid)['karma']
        return None

    def get_petConsumables(self, uuid):
        """
        Gets the status of how much of each pet consumable is left
        :param uuid:
        :return:
        """
        data = self.get_player_data(uuid)
        if data is not None:
            return self.get_player_data(uuid)['petConsumables']
        return None

    def get_collectibles(self, uuid):
        """
        Gets all the vanity items
        :param uuid:
        :return:
        """
        data = self.get_player_data(uuid)
        if data is not None:
            return self.get_player_data(uuid)['vanityMeta']["packages"]
        return None

    def get_housingMeta(self, uuid):
        """
        Gets all the housing related information
        :param uuid:
        :return:
        """
        data = self.get_player_data(uuid)
        if data is not None:
            return self.get_player_data(uuid)['housingMeta']
        return None

    def get_parkourCompletions(self, uuid):
        """
        Gets all the completed parkours including data they were completed at, and time it took to complete
        :param uuid:
        :return:
        """
        data = self.get_player_data(uuid)
        if data is not None:
            return self.get_player_data(uuid)['parkourCompletions']
        return None

    def get_mcVersionRp(self, uuid):
        """
        Gets last minecraft version recently played
        :param uuid:
        :return:
        """
        data = self.get_player_data(uuid)
        if data is not None:
            return self.get_player_data(uuid)['mcVersionRp']
        return None

    def get_petStats(self, uuid):
        """
        Gets hunger, exercise, thirst, name, and experience stats of all owned pets
        :param uuid:
        :return:
        """
        data = self.get_player_data(uuid)
        if data is not None:
            return self.get_player_data(uuid)['petStats']
        return None

    def get_lastClaimedReward(self, uuid):
        """
        Gets the last claimed reward time
        :param uuid:
        :return:
        """
        data = self.get_player_data(uuid)
        if data is not None:
            return self.get_player_data(uuid)['lastClaimedReward']
        return None

    def get_totalRewards(self, uuid):
        """
        Gets the total rewards claimed
        :param uuid:
        :return:
        """
        data = self.get_player_data(uuid)
        if data is not None:
            return self.get_player_data(uuid)['totalRewards']
        return None

    def get_totalDailyRewards(self, uuid):
        """
        Gets the total daily rewards claimed
        :param uuid:
        :return:
        """
        data = self.get_player_data(uuid)
        if data is not None:
            return self.get_player_data(uuid)['totalDailyRewards']
        return None


if __name__ == '__main__':
    UUID = username_to_uuid("Tammon")
    h = Player(apikey)
    print(h.get_player_data(UUID).keys())


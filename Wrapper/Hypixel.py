from typing import Optional

from .Exceptions.API import APIException
from .Exceptions.Other import PunishmentStatisticsException, CurrentPlayerCountException, CurrentLeaderboardsException, \
    ActiveBoostersException
from .HypixelModels.Achievements.Achievements import Achievements
from .HypixelModels.Achievements.GuildAchievements import GuildAchievements
from .HypixelModels.General.APIKey import APIKey
from .HypixelModels.General.Boosters import Boosters
from .HypixelModels.General.Challenges import Challenges
from .HypixelModels.General.GameInformation import GameInformation
from .HypixelModels.General.GuildPermissions import GuildPermissions
from .HypixelModels.General.Leaderboards import Leaderboards
from .HypixelModels.General.PlayerCounts import PlayerCounts
from .HypixelModels.General.PunishmentStatistics import PunishmentStatistics
from .HypixelModels.General.Quests import Quests
from .Requests.Requests import HypixelRequestMaker


class Miscellaneous(HypixelRequestMaker):
    def __init__(self, apiKey: str):
        super().__init__(apiKey)
        self.rateLimitReset = -1  # The time in seconds until the rate limit is reset
        self.rateLimitRemaining = -1  # The amount of requests left before reset
        self.rateLimit = -1

    def getApiKeyData(self, api_key: Optional[str] = None) -> APIKey:
        """ Get api key information.

        :param api_key: The API key which information is going to be retrieved from
        :type api_key: None or str
        :return: The object containing the information regarding the api key
        :rtype: APIKey
        """

        if api_key is not None:
            status_code, response = self._makeRequest("/key", params={"key": api_key})

        else:
            status_code, response = self._makeRequest("/key")

        if status_code != 200:
            raise APIException(status_code, response["cause"])

        return APIKey.parse_obj(response["record"])

    def getBoosters(self, api_key: Optional[str] = None) -> Boosters:
        """ Get information regarding boosters.

        :param api_key: The API key which information is going to be retrieved from
        :type api_key: None or str
        :return: The object containing the information regarding the boosters
        :rtype: Boosters
        """

        if api_key is not None:
            status_code, response = self._makeRequest("/boosters", params={"key": api_key})

        else:
            status_code, response = self._makeRequest("/boosters")

        if status_code != 200:
            raise ActiveBoostersException(status_code)

        return Boosters.parse_obj({"boosters": response["boosters"], "boosterState": response["boosterState"]})

    def getPlayerCounts(self, api_key: Optional[str] = None) -> PlayerCounts:
        """ Get player count information from various game modes and server in total.

        :param api_key: The API key which information is going to be retrieved from
        :type api_key: None or str
        :return: The object containing the information regarding player counts of the server and various game modes
        :rtype: PlayerCounts
        """

        if api_key is not None:
            status_code, response = self._makeRequest("/counts", params={"key": api_key})

        else:
            status_code, response = self._makeRequest("/counts")

        if status_code != 200:
            raise CurrentPlayerCountException(status_code)

        return PlayerCounts.parse_obj({"games": response["games"], "playerCount": response["playerCount"]})

    def getLeaderboards(self, api_key: Optional[str] = None) -> Leaderboards:
        """ Get leaderboard information.

        :param api_key: The API key which information is going to be retrieved from
        :type api_key: None or str
        :return: The object containing the information regarding the leaderboards
        :rtype: Leaderboards
        """

        if api_key is not None:
            status_code, response = self._makeRequest("/leaderboards", params={"key": api_key})

        else:
            status_code, response = self._makeRequest("/`leaderboards`")

        if status_code != 200:
            raise CurrentLeaderboardsException(status_code)

        return Leaderboards.parse_obj({"leaderboards": response["leaderboards"]})

    def getPunishmentStatistics(self, api_key: Optional[str] = None) -> PunishmentStatistics:
        """ Get punishment (watchdog or staff) information.

        :param api_key: The API key which information is going to be retrieved from
        :type api_key: None or str
        :return: The object containing the information regarding the punishment statistics
        :rtype: PunishmentStatistics
        """

        if api_key is not None:
            status_code, response = self._makeRequest("/punishmentstats", params={"key": api_key})

        else:
            status_code, response = self._makeRequest("/punishmentstats")

        if status_code != 200:
            raise PunishmentStatisticsException(status_code)

        return PunishmentStatistics.parse_obj(response)


class Resources(HypixelRequestMaker):

    def __init__(self):
        super().__init__()

    def getGameInformation(self) -> GameInformation:
        """ Get information regarding each game information.

        :return: The object containing the information regarding all hypixel games
        :rtype: GuildAchievements
        """

        status_code, response = self._makeRequest("/resources/games", apiKeyNeeded=False)

        if status_code != 200:
            raise APIException(status_code, response["cause"])

        return GameInformation.parse_obj({"lastUpdated": response["lastUpdated"], "games": response["games"]})

    def getAchievements(self) -> Achievements:
        """ Get information regarding each achievement information.

        :return: The object containing the information regarding all hypixel player achievements
        :rtype: Achievements
        """

        status_code, response = self._makeRequest("/resources/achievements", apiKeyNeeded=False)

        if status_code != 200:
            raise APIException(status_code, response["cause"])

        return Achievements.parse_obj(
            {"lastUpdated": response["lastUpdated"], "achievements": response["achievements"]})

    def getChallenges(self) -> Challenges:
        """ Get information regarding each challenges information.

        :return: The object containing the information regarding all hypixel player challenges
        :rtype: Challenges
        """

        status_code, response = self._makeRequest("/resources/challenges", apiKeyNeeded=False)

        if status_code != 200:
            raise APIException(status_code, response["cause"])

        return Challenges.parse_obj({"lastUpdated": response["lastUpdated"], "challenges": response["challenges"]})

    def getQuests(self) -> Quests:
        """ Get information regarding each quest information.

        :return: The object containing the information regarding all hypixel player quests
        :rtype: Quests
        """

        status_code, response = self._makeRequest("/resources/quests", apiKeyNeeded=False)

        if status_code != 200:
            raise APIException(status_code, response["cause"])

        return Quests.parse_obj({"lastUpdated": response["lastUpdated"], "quests": response["quests"]})

    def getGuildAchievements(self) -> GuildAchievements:
        """ Get available guild achievement information.

        :return: The object containing the information regarding which guild achievement is achievable
        :rtype: GuildAchievements
        """

        status_code, response = self._makeRequest("/resources/guilds/achievements", apiKeyNeeded=False)

        if status_code != 200:
            raise APIException(status_code, response["cause"])

        return GuildAchievements.parse_obj(
            {"lastUpdated": response["lastUpdated"], "one_time": response["one_time"], "tiered": response["tiered"]})

    def getGuildPermissions(self) -> GuildPermissions:
        """ Get available guild permission information.

        :return: The object containing the information regarding which guild permission is available
        :rtype: GuildPermissions
        """

        status_code, response = self._makeRequest("/resources/guilds/permissions", apiKeyNeeded=False)

        if status_code != 200:
            raise APIException(status_code, response["cause"])

        return GuildPermissions.parse_obj(
            {"lastUpdated": response["lastUpdated"], "permissions": response["permissions"]})


class PlayerData(HypixelRequestMaker):

    def __init__(self, apiKey: str):
        super().__init__(apiKey)



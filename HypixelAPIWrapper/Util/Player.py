from HypixelAPIWrapper.Util.Exceptions import InvalidAPIKeyError
from HypixelAPIWrapper.Util.HelperFunctions import *
import requests


class Player:
    """ Generally dates are stored as a Unix Epoch times in milliseconds. """

    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.hypixel.net/player"

    def template(self, request_type, uuid):
        """ A template function to retrieve data of type request_type"""

        data = self.get_player_data(uuid)

        if data is not None:
            return data[request_type]
        return None

    def get_player_data(self, uuid):
        """ Gets all the data of a user, optionally can cache the results and not return the results
        caching results overwrites already cached attributes """

        if not is_api_key_valid(self.api_key):
            raise InvalidAPIKeyError

        params = {"uuid": uuid, "key": self.api_key}
        r = requests.get(self.url, params=params).json()
        if r['success']:
            return r['player']
        return r['cause'] if "cause" in r else None

    def get_player_name(self, uuid):
        """ Gets the player name of a user (uuid -> player name) """

        return self.template("playername", uuid)

    def get_firstLogin(self, uuid):
        """ Gets the first Hypixel logon time """

        return self.template("firstLogin", uuid)


    def get_lastLogin(self, uuid, get_from_cache=False):
        """
        Gets player last logon time
        :param get_from_cache:
        :param uuid: UUID of player
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['lastLogin']
        return None

    def get_lastLogout(self, uuid, get_from_cache=False):
        """
        Gets player last logout time
        :param get_from_cache:
        :param uuid: UUID of player
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['lastLogout']
        return None

    def get_display_name(self, uuid, get_from_cache=False):
        """
        Gets the display name of a user
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['displayname']
        return None

    def get_achievementsOneTime(self, uuid, get_from_cache=False):
        """
        Gets all the completed one time achievements
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['achievementsOneTime']
        return None

    def get_achievements(self, uuid, get_from_cache=False):
        """
        Gets all the progress of tiered achievements
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['achievements']
        return None

    def get_achievementTotem(self, uuid, get_from_cache=False):
        """
        Gets the players achievement totem information
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['achievementTotem']
        return None

    def get_stats(self, uuid, get_from_cache=False, game_mode_id=None):
        """
        Gets stats of all games merged
        :param get_from_cache:
        :param uuid:
        :param game_mode_id:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            if game_mode_id is not None:
                if game_mode_id not in data['stats']:
                    return None
                return data['stats'][game_mode_id]
            return data['stats']
        return None

    def get_networkExp(self, uuid, get_from_cache=False):
        """
        Gets current network exp
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['networkExp']
        return None

    def get_quests(self, uuid, get_from_cache=False, quest_id=None):
        """
        Gets all completed quests lifetime
        :param get_from_cache:
        :param uuid:
        :param quest_id:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            if quest_id is not None:
                return data['quests'][quest_id]
            return data['quests']
        return None

    def get_eugene(self, uuid, get_from_cache=False):
        """
        Gets the dailyTwoKExp
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['eugene']
        return None

    def get_karma(self, uuid, get_from_cache=False):
        """
        Gets the total karma
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['karma']
        return None

    def get_petConsumables(self, uuid, get_from_cache=False):
        """
        Gets the status of how much of each pet consumable is left
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['petConsumables']
        return None

    def get_collectibles(self, uuid, get_from_cache=False):
        """
        Gets all the vanity items
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['vanityMeta']["packages"]
        return None

    def get_housingMeta(self, uuid, get_from_cache=False):
        """
        Gets all the housing related information
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['housingMeta']
        return None

    def get_parkourCompletions(self, uuid, get_from_cache=False):
        """
        Gets all the completed parkour including data they were completed at, and time it took to complete
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['parkourCompletions']
        return None

    def get_mcVersionRp(self, uuid, get_from_cache=False):
        """
        Gets last minecraft version recently played
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['mcVersionRp']
        return None

    def get_petStats(self, uuid, get_from_cache=False):
        """
        Gets hunger, exercise, thirst, name, and experience stats of all owned pets
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['petStats']
        return None

    def get_lastClaimedReward(self, uuid, get_from_cache=False):
        """
        Gets the last claimed reward time
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['lastClaimedReward']
        return None

    def get_totalRewards(self, uuid, get_from_cache=False):
        """
        Gets the total rewards claimed
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['totalRewards']
        return None

    def get_totalDailyRewards(self, uuid, get_from_cache=False):
        """
        Gets the total daily rewards claimed
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['totalDailyRewards']
        return None

    def get_rewardStreak(self, uuid, get_from_cache=False):
        """
        Gets the current reward streak
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['rewardStreak']
        return None

    def get_rewardScore(self, uuid, get_from_cache=False):
        """
        Gets the current reward score
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['rewardScore']
        return None

    def get_rewardHighScore(self, uuid, get_from_cache=False):
        """
        Gets the current reward high score
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['rewardHighScore']
        return None

    def get_giftingMeta(self, uuid, get_from_cache=False):
        """
        Gets information related to gifts/ranks given and received
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['giftingMeta']
        return None

    def get_adsense_tokens(self, uuid, get_from_cache=False):
        """
        Gets the adsense tokens
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['adsense_tokens']
        return None

    def get_fortuneBuff(self, uuid, get_from_cache=False):
        """
        (I think May be the radiating amount after giving a gift)
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['fortuneBuff']
        return None

    def get_flashingSalePopup(self, uuid, get_from_cache=False):
        """
        Gets the flashingSalePopup statistic
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['flashingSalePopup']
        return None

    def get_flashingSaleOpens(self, uuid, get_from_cache=False):
        """
        Gets the flashingSaleOpens statistic
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['flashingSaleOpens']
        return None

    def get_flashingSalePoppedUp(self, uuid, get_from_cache=False):
        """
        Gets the flashingSalePoppedUp statistic
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['flashingSalePoppedUp']
        return None

    def get_flashingSaleClicks(self, uuid, get_from_cache=False):
        """
        Gets the flashingSaleClicks statistic
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['flashingSaleClicks']
        return None

    def get_userLanguage(self, uuid, get_from_cache=False):
        """
        Gets the saved user language set on the network
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['userLanguage']
        return None

    def get_quick_join_uses(self, uuid, get_from_cache=False):
        """
        Gets the number of quick join uses
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['quickjoin_uses']
        return None

    def get_quick_join_timestamp(self, uuid, get_from_cache=False):
        """
        Gets the quick join timestamp
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['quickjoin_timestamp']
        return None

    def get_santa_quest_started(self, uuid, get_from_cache=False):
        """
        Gets the state of the santa quest where True means started
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['SANTA_QUEST_STARTED']
        return None

    def get_santa_finished(self, uuid, get_from_cache=False):
        """
        Gets the state of the santa quest where True means finished
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['SANTA_FINISHED']
        return None

    def get_compassStats(self, uuid, get_from_cache=False):
        """
        Gets the compass stats
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['compassStats']
        return None

    def get_newPackageRank(self, uuid, get_from_cache=False):
        """
        Gets the current non monthly rank (highest mvp+)
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['newPackageRank']
        return None

    def get_levelUp_VIP(self, uuid, get_from_cache=False):
        """
        Gets the date and time of when the user upgraded to vip rank
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['levelUp_VIP']
        return None

    def get_levelUp_VIP_PLUS(self, uuid, get_from_cache=False):
        """
        Gets the date and time of when the user upgraded to vip+ rank
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['levelUp_VIP_PLUS']
        return None

    def get_levelUp_MVP(self, uuid, get_from_cache=False):
        """
        Gets the date and time of when the user upgraded to mvp rank
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['levelUp_MVP']
        return None

    def get_levelUp_MVP_PLUS(self, uuid, get_from_cache=False):
        """
        Gets the date and time of when the user upgraded to mvp+ rank
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['levelUp_MVP_PLUS']
        return None

    def get_rankPlusColor(self, uuid, get_from_cache=False):
        """
        Gets the colour of the rank plus
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['rankPlusColor']
        return None

    def get_challenges(self, uuid, get_from_cache=False):
        """
        Gets all the challenges completed and how many times they were completed
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['challenges']
        return None

    def get_channel(self, uuid, get_from_cache=False):
        """
        Gets the chat channel currently selected, ALL, PARTY, GUILD, STAFF, CO-OP
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['channel']
        return None

    def get_mostRecentlyTippedUuid(self, uuid, get_from_cache=False):
        """
        Gets the uuid of the most recently tipped player
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['mostRecentlyTippedUuid']
        return None

    def get_achievementPoints(self, uuid, get_from_cache=False):
        """
        Gets the number of achievement points excluding legacy achievements
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['achievementPoints']
        return None

    def get_outfit(self, uuid, get_from_cache=False):
        """
        Gets the current outfit of the player
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['outfit']
        return None

    def get_currentCloak(self, uuid, get_from_cache=False):
        """
        Gets the current selected cloak
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['currentCloak']
        return None

    def get_currentPet(self, uuid, get_from_cache=False):
        """
        Gets the current selected pet
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['currentPet']
        return None

    def get_particlePack(self, uuid, get_from_cache=False):
        """
        Gets the current selected particle pack
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['particlePack']
        return None

    def get_socialMedia(self, uuid, get_from_cache=False):
        """
        Gets all the linked social media details
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['socialMedia']
        return None

    def get_questSettings(self, uuid, get_from_cache=False):
        """
        Gets whether autoActivate quests is toggled on (True) or not
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['questSettings']
        return None

    def get_currentGadget(self, uuid, get_from_cache=False):
        """
        Gets the current selected gadget
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['currentGadget']
        return None

    def get_currentClickEffect(self, uuid, get_from_cache=False):
        """
        Gets the current selected click effect
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['currentClickEffect']
        return None

    def get_mostRecentGameType(self, uuid, get_from_cache=False):
        """
        Gets the most recent game type
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['mostRecentGameType']
        return None

    def get_tourney(self, uuid, get_from_cache=False):
        """
        Gets the tournament information
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['tourney']
        return None

    def get_monthly_crates(self, uuid, get_from_cache=False):
        """
        Gets the monthly crate information
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['monthlycrates']
        return None

    def get_rewardConsumed(self, uuid, get_from_cache=False):
        """
        Gets the state of the reward
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['rewardConsumed']
        return None

    def get_achievementTracking(self, uuid, get_from_cache=False):
        """
        Gets all achievements being tracked
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['achievementTracking']
        return None

    def get_achievementRewardsNew(self, uuid, get_from_cache=False):
        """
        Gets all achievement rewards claimed and the time they were claimed at
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['achievementRewardsNew']
        return None

    def get_parkourCheckpointBests(self, uuid, get_from_cache=False):
        """
        Gets the best parkour checkpoint times
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['parkourCheckpointBests']
        return None

    def get_vanityFirstConvertedBox(self, uuid, get_from_cache=False):
        """
        Gets the time first converted box was converted at
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['vanityFirstConvertedBox']
        return None

    def get_petJourneyTimestamp(self, uuid, get_from_cache=False):
        """
        Gets the pet Journey Timestamp
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['petJourneyTimestamp']
        return None

    def get_vanityConvertedBoxToday(self, uuid, get_from_cache=False):
        """
        Gets the vanity converted box amount today
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['vanityConvertedBoxToday']
        return None

    def get_friendRequestsUuid(self, uuid, get_from_cache=False):
        """
        Gets all pending friend request uuids
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['friendRequestsUuid']
        return None

    def get_adventRewards(self, uuid, year, get_from_cache=False):
        """
        Gets all advent rewards collected with timestamp of year provided
        :param get_from_cache:
        :param year:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data[f'adventRewards{year}']
        return None

    def get_completed_christmas_quests(self, uuid, year, get_from_cache=False):
        """
        Gets the number of completed christmas quest of a given year
        :param year:
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data[f'completed_christmas_quests_{year}']
        return None

    def get_onetime_achievement_menu_sort(self, uuid, get_from_cache=False):
        """
        Gets the sorting method for one time achievements
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['onetime_achievement_menu_sort']
        return None

    def get_tiered_achievement_menu_sort(self, uuid, get_from_cache=False):
        """
        Gets the sorting method for tiered achievement menu
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['tiered_achievement_menu_sort']
        return None

    def get_onetime_achievement_menu_sort_completion_sort(self, uuid, get_from_cache=False):
        """
        Gets the sorting method for onetime achievement menu completion
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['onetime_achievement_menu_sort_completion_sort']
        return None

    def get_lastAdsenseGenerateTime(self, uuid, get_from_cache=False):
        """
        Gets the last adsense generation time
        :param get_from_cache:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data['lastAdsenseGenerateTime']
        return None

    def get_levelingReward(self, uuid, level, get_from_cache=False):
        """
        Gets the leveling reward if claimed for a given level if reward exists
        :param get_from_cache:
        :param level:
        :param uuid:
        :return:
        """
        if get_from_cache:
            state, msg = self.isDataAlreadyCached(uuid)
            if state:
                data = self.cached_data
            else:
                print(msg)
                return
        else:
            data = self.get_player_data(uuid)

        if data is not None:
            return data[f'levelingReward_{level}']
        return None


if __name__ == '__main__':
    # example usage
    # apikey = ""
    UUID = username_to_uuid("Tammon")
    h = Player(apikey)

    # what happens if you call from cache but nothing is cached
    print(h.get_outfit(UUID, get_from_cache=True))
    print()

    # caching
    h.get_player_data(UUID, cache_results=True, return_result_if_cached=False)

    # example function usage
    print(h.get_achievementPoints(UUID, get_from_cache=True))
    print(h.get_networkExp(UUID, get_from_cache=True))

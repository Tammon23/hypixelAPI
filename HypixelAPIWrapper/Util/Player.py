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
            if request_type in data:
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

    def get_lastLogin(self, uuid):
        """ Gets player last logon time """

        return self.template("lastLogin", uuid)

    def get_lastLogout(self, uuid):
        """ Gets player last logout time """

        return self.template("lastLogout", uuid)

    def get_display_name(self, uuid):
        """ Gets the display name of a user """

        return self.template("displayname", uuid)

    def get_achievementsOneTime(self, uuid):
        """ Gets all the completed one time achievements """

        return self.template("achievementsOneTime", uuid)

    def get_achievements(self, uuid):
        """ Gets all the progress of tiered achievements """

        return self.template("achievements", uuid)

    def get_achievementTotem(self, uuid):
        """ Gets the players achievement totem information """

        return self.template("achievementTotem", uuid)

    def get_stats(self, uuid, game_mode_id=None):
        """ Gets stats of all games merged """

        data = self.get_player_data(uuid)

        if data is not None:
            if game_mode_id is not None:
                if game_mode_id not in data['stats']:
                    return None
                return data['stats'][game_mode_id]
            return data['stats']
        return None

    def get_networkExp(self, uuid):
        """ Gets current network exp """

        return self.template("networkExp", uuid)

    def get_quests(self, uuid, quest_id=None):
        """ Gets all completed quests lifetime """

        data = self.get_player_data(uuid)

        if data is not None:
            if quest_id is not None:
                if quest_id not in data['quests']:
                    return None
                return data['quests'][quest_id]
            return data['quests']
        return None

    def get_eugene(self, uuid):
        """ Gets the dailyTwoKExp """

        return self.template("eugene", uuid)

    def get_karma(self, uuid):
        """ Gets the total karma """

        return self.template("karma", uuid)

    def get_petConsumables(self, uuid):
        """ Gets the status of how much of each pet consumable is left """

        return self.template("petConsumables", uuid)

    def get_collectibles(self, uuid):
        """ Gets all the vanity items """

        data = self.get_player_data(uuid)

        if data is not None:
            return data['vanityMeta']["packages"]
        return None

    def get_housingMeta(self, uuid):
        """ Gets all the housing related information """

        return self.template('housingMeta', uuid)

    def get_parkourCompletions(self, uuid):
        """ Gets all the completed parkour including data they were completed at, and time it took to complete """

        return self.template("parkourCompletions", uuid)

    def get_mcVersionRp(self, uuid):
        """ Gets last minecraft version recently played """

        return self.template("mcVersionRp", uuid)

    def get_petStats(self, uuid):
        """ Gets hunger, exercise, thirst, name, and experience stats of all owned pets """

        return self.template("petStats", uuid)

    def get_lastClaimedReward(self, uuid):
        """ Gets the last claimed reward time """

        return self.template("lastClaimedReward", uuid)

    def get_totalRewards(self, uuid):
        """ Gets the total rewards claimed """

        return self.template("totalRewards", uuid)

    def get_totalDailyRewards(self, uuid):
        """ Gets the total daily rewards claimed """

        return self.template("totalDailyRewards", uuid)

    def get_rewardStreak(self, uuid):
        """ Gets the current reward streak """

        return self.template("rewardStreak", uuid)

    def get_rewardScore(self, uuid):
        """ Gets the current reward score """

        return self.template("rewardScore", uuid)

    def get_rewardHighScore(self, uuid):
        """ Gets the current reward high score """

        return self.template("rewardHighScore", uuid)

    def get_giftingMeta(self, uuid):
        """ Gets information related to gifts/ranks given and received """

        return self.template("giftingMeta", uuid)

    def get_adsense_tokens(self, uuid):
        """ Gets the adsense tokens """

        return self.template('adsense_tokens', uuid)

    def get_fortuneBuff(self, uuid):
        """(I think May be the radiating amount after giving a gift) """

        return self.template('fortuneBuff', uuid)

    def get_flashingSalePopup(self, uuid):
        """ Gets the flashingSalePopup statistic """

        return self.template('flashingSalePopup', uuid)

    def get_flashingSaleOpens(self, uuid):
        """ Gets the flashingSaleOpens statistic """

        return self.template('flashingSaleOpens', uuid)

    def get_flashingSalePoppedUp(self, uuid):
        """ Gets the flashingSalePoppedUp statistic """

        return self.template('flashingSalePoppedUp', uuid)

    def get_flashingSaleClicks(self, uuid):
        """ Gets the flashingSaleClicks statistic """

        return self.template('flashingSaleClicks', uuid)

    def get_userLanguage(self, uuid):
        """ Gets the saved user language set on the network """

        return self.template('userLanguage', uuid)

    def get_quick_join_uses(self, uuid):
        """ Gets the number of quick join uses """

        return self.template('quickjoin_uses', uuid)

    def get_quick_join_timestamp(self, uuid):
        """ Gets the quick join timestamp """

        return self.template('quickjoin_timestamp', uuid)

    def get_santa_quest_started(self, uuid):
        """ Gets the state of the santa quest where True means started """

        return self.template('SANTA_QUEST_STARTED', uuid)

    def get_santa_finished(self, uuid):
        """ Gets the state of the santa quest where True means finished """

        return self.template('SANTA_FINISHED', uuid)

    def get_compassStats(self, uuid):
        """ Gets the compass stats """

        return self.template('compassStats', uuid)

    def get_newPackageRank(self, uuid):
        """ Gets the current non monthly rank (highest mvp+) """

        return self.template('newPackageRank', uuid)

    def get_levelUp_VIP(self, uuid):
        """ Gets the date and time of when the user upgraded to vip rank """

        return self.template('levelUp_VIP', uuid)

    def get_levelUp_VIP_PLUS(self, uuid):
        """ Gets the date and time of when the user upgraded to vip+ rank """

        return self.template('levelUp_VIP_PLUS', uuid)

    def get_levelUp_MVP(self, uuid):
        """ Gets the date and time of when the user upgraded to mvp rank """

        return self.template('levelUp_MVP', uuid)

    def get_levelUp_MVP_PLUS(self, uuid):
        """ Gets the date and time of when the user upgraded to mvp+ rank """

        return self.template('levelUp_MVP_PLUS', uuid)

    def get_rankPlusColor(self, uuid):
        """ Gets the colour of the rank plus """

        return self.template('rankPlusColor', uuid)

    def get_challenges(self, uuid):
        """ Gets all the challenges completed and how many times they were completed """

        return self.template('challenges', uuid)

    def get_channel(self, uuid):
        """ Gets the chat channel currently selected, ALL, PARTY, GUILD, STAFF, CO-OP """

        return self.template('channel', uuid)

    def get_mostRecentlyTippedUuid(self, uuid):
        """ Gets the uuid of the most recently tipped player """

        return self.template('mostRecentlyTippedUuid', uuid)

    def get_achievementPoints(self, uuid):
        """ Gets the number of achievement points excluding legacy achievements """

        return self.template('achievementPoints', uuid)

    def get_outfit(self, uuid):
        """ Gets the current outfit of the player """

        return self.template('outfit', uuid)

    def get_currentCloak(self, uuid):
        """ Gets the current selected cloak """

        return self.template('currentCloak', uuid)

    def get_currentPet(self, uuid):
        """ Gets the current selected pet """

        return self.template('currentPet', uuid)

    def get_particlePack(self, uuid):
        """ Gets the current selected particle pack """

        return self.template('particlePack', uuid)

    def get_socialMedia(self, uuid):
        """ Gets all the linked social media details """

        return self.template('socialMedia', uuid)

    def get_questSettings(self, uuid):
        """ Gets whether autoActivate quests is toggled on (True) or not """

        return self.template('questSettings', uuid)

    def get_currentGadget(self, uuid):
        """ Gets the current selected gadget """

        return self.template('currentGadget', uuid)

    def get_currentClickEffect(self, uuid):
        """ Gets the current selected click effect """

        return self.template('currentClickEffect', uuid)

    def get_mostRecentGameType(self, uuid):
        """ Gets the most recent game type """

        return self.template('mostRecentGameType', uuid)

    def get_tourney(self, uuid):
        """ Gets the tournament information """

        return self.template('tourney', uuid)

    def get_monthly_crates(self, uuid):
        """ Gets the monthly crate information """

        return self.template('monthlycrates', uuid)

    def get_rewardConsumed(self, uuid):
        """ Gets the state of the reward """

        return self.template('rewardConsumed', uuid)

    def get_achievementTracking(self, uuid):
        """ Gets all achievements being tracked """

        return self.template('achievementTracking', uuid)

    def get_achievementRewardsNew(self, uuid):
        """ Gets all achievement rewards claimed and the time they were claimed at """

        return self.template('achievementRewardsNew', uuid)

    def get_parkourCheckpointBests(self, uuid):
        """ Gets the best parkour checkpoint times """

        return self.template('parkourCheckpointBests', uuid)

    def get_vanityFirstConvertedBox(self, uuid):
        """ Gets the time first converted box was converted at """

        return self.template('vanityFirstConvertedBox', uuid)

    def get_petJourneyTimestamp(self, uuid):
        """ Gets the pet Journey Timestamp """

        return self.template('petJourneyTimestamp', uuid)

    def get_vanityConvertedBoxToday(self, uuid):
        """ Gets the vanity converted box amount today """

        return self.template('vanityConvertedBoxToday', uuid)

    def get_friendRequestsUuid(self, uuid):
        """ Gets all pending friend request uuids """

        return self.template('friendRequestsUuid', uuid)

    def get_adventRewards(self, uuid, year):
        """ Gets all advent rewards collected with timestamp of year provided """

        return self.template(f'adventRewards{year}', uuid)

    def get_completed_christmas_quests(self, uuid, year):
        """ Gets the number of completed christmas quest of a given year """

        return self.template(f'completed_christmas_quests_{year}', uuid)

    def get_onetime_achievement_menu_sort(self, uuid):
        """ Gets the sorting method for one time achievements """

        return self.template('onetime_achievement_menu_sort', uuid)

    def get_tiered_achievement_menu_sort(self, uuid):
        """ Gets the sorting method for tiered achievement menu """

        return self.template('tiered_achievement_menu_sort', uuid)

    def get_onetime_achievement_menu_sort_completion_sort(self, uuid):
        """ Gets the sorting method for onetime achievement menu completion """

        return self.template('onetime_achievement_menu_sort_completion_sort', uuid)

    def get_lastAdsenseGenerateTime(self, uuid):
        """ Gets the last adsense generation time """

        return self.template("lastAdsenseGenerateTime", uuid)

    def get_levelingReward(self, uuid, level):
        """ Gets the leveling reward if claimed for a given level if reward exists """

        return self.template(f'levelingReward_{level}', uuid)


if __name__ == '__main__':
    # example usage
    # apikey = ""
    UUID = username_to_uuid("Tammon")
    h = Player(apikey)

    # example function usage
    print(h.get_achievementPoints(UUID))
    print(h.get_networkExp(UUID))

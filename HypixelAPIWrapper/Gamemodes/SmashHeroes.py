from HypixelAPIWrapper.Util import Player
from enum import Enum
from HypixelAPIWrapper.Util._SmashHeroesUtil import *


class Heroes(Enum):
    BULK = "THE_BULK"
    GENERAL_CLUCK = "GENERAL_CLUCK"
    CAKE_MONSTER = "CAKE_MONSTER"
    BOTMON = "BOTMUN"
    TINMAN = "TINMAN"
    SERGEANT_SHIELD = "SERGEANT_SHIELD"
    CRYOMANCER = "FROSTY"
    SKULLFIRE = "SKULLFIRE"
    SANIC = "SANIC"
    KARAKOT = "GOKU"
    PUG = "PUG"
    SPODERMAN = "SPODERMAN"
    MARAUDER = "MARAUDER"
    SHOOP = "SHOOP_DA_WHOOP"
    GREEN_HOOD = "GREEN_HOOD"
    VOID_CRAWLER = "DUSK_CRAWLER"


class SmashHeroes:
    """ If an attribute is not in the Hypixel database, will return None"""

    def __init__(self, api_key):
        self.api_key = api_key
        self.player = Player.Player(api_key)
        self.gamemode_name = "SuperSmash"

    @staticmethod
    def get_play_command_1v1v1v1():
        return "/play super_smash_solo_normal"

    @staticmethod
    def get_play_command_2v2():
        return "/play super_smash_2v2_normal"

    @staticmethod
    def get_play_command_2v2v2():
        return "/play super_smash_teams_normal"

    @staticmethod
    def get_play_command_friends():
        return "/play super_smash_friends_normal"

    def get_stats(self, uuid, get_from_cache=False):
        stats = self.player.get_stats(uuid, get_from_cache, self.gamemode_name)

        return stats

    def template(self, uuid, get_from_cache, attribute_id):
        """ A template function """
        stats = self.get_stats(uuid, get_from_cache)
        if attribute_id not in stats:
            return None

        return stats[attribute_id]

    def get_smash_level(self, uuid, get_from_cache=False):
        """ Returns the smash level of a user (the sum of all levels of each hero) """

        return self.template(uuid, get_from_cache, "smashLevel")

    def get_active_class(self, uuid, get_from_cache=False):
        """ Returns the currently selected class of the user """

        return self.template(uuid, get_from_cache, "active_class")

    def get_winstreak_overall(self, uuid, get_from_cache=False):
        """ Returns the current winstreak considering all gamemodes """

        return self.template(uuid, get_from_cache, "win_streak")

    def get_deaths_overall(self, uuid, get_from_cache=False):
        """ Returns the number of overall deaths """

        return self.template(uuid, get_from_cache, "deaths")

    def get_deaths_1v1v1v1(self, uuid, get_from_cache=False):
        """ Returns the number of 1v1v1v1 deaths """

        return self.template(uuid, get_from_cache, "deaths_normal")

    def get_deaths_2v2(self, uuid, get_from_cache=False):
        """ Returns the number of 2v2 deaths """

        return self.template(uuid, get_from_cache, "deaths_2v2")

    def get_deaths_2v2v2(self, uuid, get_from_cache=False):
        """ Returns the number of 2v2 deaths """

        return self.template(uuid, get_from_cache, "deaths_teams")

    def get_kills_overall(self, uuid, get_from_cache=False):
        """ Returns the number of overall kills """

        return self.template(uuid, get_from_cache, "kills")

    def get_kills_1v1v1v1(self, uuid, get_from_cache=False):
        """ Returns the number of 1v1v1v1 kills """

        return self.template(uuid, get_from_cache, "kills_normal")

    def get_kills_2v2(self, uuid, get_from_cache=False):
        """ Returns the number of 2v2 kills """

        return self.template(uuid, get_from_cache, "kills_2v2")

    def get_kills_2v2v2(self, uuid, get_from_cache=False):
        """ Returns the number of 2v2v2 kills """

        return self.template(uuid, get_from_cache, "kills_teams")

    def get_losses_overall(self, uuid, get_from_cache=False):
        """ Returns the number of overall losses """

        return self.template(uuid, get_from_cache, "losses")

    def get_losses_1v1v1v1(self, uuid, get_from_cache=False):
        """ Returns the number of 1v1v1v1 losses """

        return self.template(uuid, get_from_cache, "losses_normal")

    def get_losses_2v2(self, uuid, get_from_cache=False):
        """ Returns the number of 2v2 losses """

        return self.template(uuid, get_from_cache, "losses_2v2")

    def get_losses_2v2v2(self, uuid, get_from_cache=False):
        """ Returns the number of 2v2v2 losses """

        return self.template(uuid, get_from_cache, "losses_teams")

    def get_wins_overall(self, uuid, get_from_cache=False):
        """ Returns the number of overall wins """

        return self.template(uuid, get_from_cache, "wins")

    def get_wins_1v1v1v1(self, uuid, get_from_cache=False):
        """ Returns the number of 1v1v1v1 wins """

        return self.template(uuid, get_from_cache, "wins_normal")

    def get_wins_2v2(self, uuid, get_from_cache=False):
        """ Returns the number of 2v2 wins """

        return self.template(uuid, get_from_cache, "wins_2v2")

    def get_wins_2v2v2(self, uuid, get_from_cache=False):
        """ Returns the number of 2v2v2 wins """

        return self.template(uuid, get_from_cache, "wins_teams")

    def get_coins(self, uuid, get_from_cache=False):
        """ Returns the number of coins """

        return self.template(uuid, get_from_cache, "coins")

    def get_quits(self, uuid, get_from_cache=False):
        """ Returns the number of quits """

        return self.template(uuid, get_from_cache, "quits")

    def get_games_overall(self, uuid, get_from_cache=False):
        """ Returns the number of overall games played
            (might also include friends mode and 1v1 mode) """

        return self.template(uuid, get_from_cache, "games")

    def get_games_1v1v1v1(self, uuid, get_from_cache=False):
        """ Returns the number of 1v1v1v1 games played  """

        return self.template(uuid, get_from_cache, "games_normal")

    def get_games_2v2(self, uuid, get_from_cache=False):
        """ Returns the number of 2v2 games played  """

        return self.template(uuid, get_from_cache, "games_2v2")

    def get_games_2v2v2(self, uuid, get_from_cache=False):
        """ Returns the number of 2v2v2 games played  """

        return self.template(uuid, get_from_cache, "games_teams")

    def get_damage_dealt_overall(self, uuid, get_from_cache=False):
        """ Returns the damage dealt overall """

        return self.template(uuid, get_from_cache, "damage_dealt")

    def get_damage_dealt_2v2(self, uuid, get_from_cache=False):
        """ Returns the damage dealt in 2v2 """

        return self.template(uuid, get_from_cache, "damage_dealt_2v2")

    def get_damage_dealt_1v1v1v1(self, uuid, get_from_cache=False):
        """ Returns the damage dealt in 1v1v1v1 """

        return self.template(uuid, get_from_cache, "damage_dealt_normal")

    def get_hero_xp(self, uuid, hero, get_from_cache=False):
        """ Returns the xp of a provided hero """

        return self.template(uuid, get_from_cache, "xp_" + hero)

    def get_hero_prestige(self, uuid, hero, get_from_cache=False):
        """ Returns the prestige level of a provided hero """

        return self.template(uuid, get_from_cache, "pg_" + hero)

    def get_hero_level(self, uuid, hero, get_from_cache=False):
        """ Returns the level of a provided hero """

        return self.template(uuid, get_from_cache, "lastLevel_" + hero)

    def is_hero_masterskin_enabled(self, uuid, hero, get_from_cache=False):
        """ Checks to see if a hero has their masterskin enabled """

        return self.template(uuid, get_from_cache, "masterArmor_" + hero)

    def get_number_of_10_plays_exp_boosters_bought(self, uuid, get_from_cache=False):
        """ Returns the number of 10 plays exp booster purchased """

        return self.template(uuid, get_from_cache, "expBooster_purchases_10_plays")

    def get_number_of_30_plays_exp_boosters_bought(self, uuid, get_from_cache=False):
        """ Returns the number of 30 plays exp booster purchased """

        return self.template(uuid, get_from_cache, "expBooster_purchases_30_plays")

    def get_number_of_50_plays_exp_boosters_bought(self, uuid, get_from_cache=False):
        """ Returns the number of 50 plays exp booster purchased """

        return self.template(uuid, get_from_cache, "expBooster_purchases_50_plays")

    def get_number_of_100_plays_exp_boosters_bought(self, uuid, get_from_cache=False):
        """ Returns the number of 100 plays exp booster purchased """

        return self.template(uuid, get_from_cache, "expBooster_purchases_100_plays")

    def get_hero(self, uuid, hero, get_from_cache=False):
        """ Returns the hero class associated to the provided hero """

        # I can't wait for case statements in python (3.10)
        if hero == Heroes.BULK:
            return Bulk(self.api_key, uuid)

        elif hero == Heroes.GENERAL_CLUCK:
            return GeneralCluck(self.api_key, uuid)

        elif hero == Heroes.CAKE_MONSTER:
            return CakeMonster(self.api_key, uuid)

        elif hero == Heroes.BOTMON:
            return Botmon(self.api_key, uuid)

        elif hero == Heroes.TINMAN:
            return Tinman(self.api_key, uuid)

        elif hero == Heroes.SERGEANT_SHIELD:
            return SergentShield(self.api_key, uuid)

        elif hero == Heroes.CRYOMANCER:
            return Cryomancer(self.api_key, uuid)

        elif hero == Heroes.SKULLFIRE:
            return Skullfire(self.api_key, uuid)

        elif hero == Heroes.SANIC:
            return Sanic(self.api_key, uuid)

        elif hero == Heroes.KARAKOT:
            return Karakot(self.api_key, uuid)

        elif hero == Heroes.PUG:
            return Pug(self.api_key, uuid)

        elif hero == Heroes.SPODERMAN:
            return Spooderman(self.api_key, uuid)

        elif hero == Heroes.MARAUDER:
            return Marauder(self.api_key, uuid)

        elif hero == Heroes.SHOOP:
            return Shoop(self.api_key, uuid)

        elif hero == Heroes.GREEN_HOOD:
            return GreenHood(self.api_key, uuid)

        elif hero == Heroes.VOID_CRAWLER:
            return VoidCrawler(self.api_key, uuid)

        else:
            return None


"""
Unused attributes

Probably Deprecated? 
- smashed_normal
- smasher_normal
- smashed
- smasher
- smashed_2v2
- smasher_2v2
- smashed_normal
- smashed_teams
- smasher_teams

- votes_Color Clash
- votes_Agora
- votes_Marshland
- votes_Strawberry Towers
- votes_Apex
- votes_Circled
- votes_Toybox
- votes_Remains
- votes_Skyline
- votes_Cobalt
- votes_Courtyard
- votes_Triplets

Duplicated
- smash_level_total = smashLevel

"""

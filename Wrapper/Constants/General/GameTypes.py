from enum import Enum
from dataclasses import dataclass


@dataclass
class _GameType:
    ID: int
    TYPE_NAME: str
    DATABASE_NAME: str
    CLEAN_NAME: str


class GameTypes(Enum):
    ARCADE = _GameType(14, "ARCADE", "Arcade", "Arcade")
    ARENA = _GameType(17, "ARENA", "Arena", "Arena")
    BATTLEGROUND = _GameType(23, "BATTLEGROUND", "Battleground", "Warlords")
    BEDWARS = _GameType(58, "BEDWARS", "Bedwars", "Bed Wars")
    BUILD_BATTLE = _GameType(60, "BUILD_BATTLE", "BuildBattle", "Build Battle")
    DUELS = _GameType(61, "DUELS", "BuildBattle", "Build Battle")
    GINGERBREAD = _GameType(25, "GINGERBREAD", "GingerBread", "Turbo Kart Racers")
    HOUSING = _GameType(26, "HOUSING", "Housing", "Housing")
    LEGACY = _GameType(56, "LEGACY", "Legacy", "Classic Games")
    MCGO = _GameType(21, "MCGO", "MCGO", "Cops and Crims")
    MURDER_MYSTERY = _GameType(59, "MURDER_MYSTERY", "MurderMystery", "Murder Mystery")
    PAINTBALL = _GameType(4, "PAINTBALL", "Paintball", "Paintball")
    PIT = _GameType(64, "PIT", "Pit", "Pit")
    PROTOTYPE = _GameType(57, "PROTOTYPE", "Prototype", "Prototype")
    QUAKECRAFT = _GameType(2, "QUAKECRAFT", "Quake", "Quake")
    REPLAY = _GameType(65, "REPLAY", "Replay", "Replay")
    SKYBLOCK = _GameType(63, "SKYBLOCK", "SkyBlock", "SkyBlock")
    SKYCLASH = _GameType(55, "SKYCLASH", "SkyClash", "SkyClash")
    SKYWARS = _GameType(51, "SKYWARS", "SkyWars", "SkyWars")
    SMP = _GameType(67, "SMP", "SMP", "SMP")
    SPEED_UHC = _GameType(54, "SPEED_UHC", "SpeedUHC", "Speed UHC")
    SUPER_SMASH = _GameType(24, "SUPER_SMASH", "SuperSmash", "Smash Heroes")
    SURVIVAL_GAMES = _GameType(5, "SURVIVAL_GAMES", "HungerGames", "Blitz Survival Games")
    TNTGAMES = _GameType(6, "TNTGAMES", "TNTGames", "TNT Games")
    TRUE_COMBAT = _GameType(52, "TRUE_COMBAT", "TrueCombat", "Crazy Walls")
    UHC = _GameType(20, "UHC", "UHC", "UHC Champions")
    VAMPIREZ = _GameType(7, "VAMPIREZ", "VampireZ", "VampireZ")
    WALLS = _GameType(3, "WALLS", "Walls", "Walls")
    WALLS3 = _GameType(13, "WALLS3", "Walls3", "Mega Walls")

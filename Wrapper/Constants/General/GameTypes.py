from typing import NamedTuple, Dict, Tuple


class GameType(NamedTuple):
    ID: int
    TYPE_NAME: str
    DATABASE_NAME: str
    CLEAN_NAME: str
    LOBBY_NAME: str = ""
    LOBBY_NAME_ALIASES: Tuple[str, ...] = ()
    PLAY_COMMANDS: Dict[str, str] = {}


ARCADE = GameType(14, "ARCADE", "Arcade", "Arcade")
ARENA = GameType(17, "ARENA", "Arena", "Arena")
BATTLEGROUND = GameType(23, "BATTLEGROUND", "Battleground", "Warlords")
BEDWARS = GameType(58, "BEDWARS", "Bedwars", "Bed Wars")
BUILD_BATTLE = GameType(60, "BUILD_BATTLE", "BuildBattle", "Build Battle")
DUELS = GameType(61, "DUELS", "BuildBattle", "Build Battle")
GINGERBREAD = GameType(25, "GINGERBREAD", "GingerBread", "Turbo Kart Racers")
HOUSING = GameType(26, "HOUSING", "Housing", "Housing")
LEGACY = GameType(56, "LEGACY", "Legacy", "Classic Games")
MCGO = GameType(21, "MCGO", "MCGO", "Cops and Crims")
MURDER_MYSTERY = GameType(59, "MURDER_MYSTERY", "MurderMystery", "Murder Mystery")
PAINTBALL = GameType(4, "PAINTBALL", "Paintball", "Paintball")
PIT = GameType(64, "PIT", "Pit", "Pit")
PROTOTYPE = GameType(57, "PROTOTYPE", "Prototype", "Prototype")
QUAKECRAFT = GameType(2, "QUAKECRAFT", "Quake", "Quake")
REPLAY = GameType(65, "REPLAY", "Replay", "Replay")
SKYBLOCK = GameType(63, "SKYBLOCK", "SkyBlock", "SkyBlock")
SKYCLASH = GameType(55, "SKYCLASH", "SkyClash", "SkyClash")
SKYWARS = GameType(51, "SKYWARS", "SkyWars", "SkyWars")
SMP = GameType(67, "SMP", "SMP", "SMP")
SPEED_UHC = GameType(54, "SPEED_UHC", "SpeedUHC", "Speed UHC")
SUPER_SMASH = GameType(24, "SUPER_SMASH", "SuperSmash", "Smash Heroes")
SURVIVAL_GAMES = GameType(5, "SURVIVAL_GAMES", "HungerGames", "Blitz Survival Games")
TNTGAMES = GameType(6, "TNTGAMES", "TNTGames", "TNT Games")
TRUE_COMBAT = GameType(52, "TRUE_COMBAT", "TrueCombat", "Crazy Walls")
UHC = GameType(20, "UHC", "UHC", "UHC Champions")
VAMPIREZ = GameType(7, "VAMPIREZ", "VampireZ", "VampireZ")
WALLS = GameType(3, "WALLS", "Walls", "Walls")
WALLS3 = GameType(13, "WALLS3", "Walls3", "Mega Walls")

GameTypeDict = {
    2: QUAKECRAFT,
    3: WALLS,
    4: PAINTBALL,
    5: SURVIVAL_GAMES,
    6: TNTGAMES,
    7: VAMPIREZ,
    13: WALLS3,
    14: ARCADE,
    17: ARENA,
    20: UHC,
    21: MCGO,
    23: BATTLEGROUND,
    24: SUPER_SMASH,
    25: GINGERBREAD,
    26: HOUSING,
    51: SKYWARS,
    52: TRUE_COMBAT,
    54: SPEED_UHC,
    55: SKYCLASH,
    56: LEGACY,
    57: PROTOTYPE,
    58: BEDWARS,
    59: MURDER_MYSTERY,
    60: BUILD_BATTLE,
    61: DUELS,
    63: SKYBLOCK,
    64: PIT,
    65: REPLAY,
    67: SMP
}

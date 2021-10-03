from typing import Dict, Optional

from pydantic import BaseModel


class GamePlayerCounts(BaseModel):
    players: int
    modes: Optional[Dict[str, int]]


class PlayerCounts(BaseModel):
    games: Dict[str, GamePlayerCounts]
    playerCount: int

from datetime import datetime
from typing import Dict

from pydantic import BaseModel

from Wrapper.HypixelModels.General.GamerJuice import GamerJuice


class GameInformation(BaseModel):
    lastUpdated: datetime
    games: Dict[str, GamerJuice]

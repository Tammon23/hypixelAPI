from datetime import datetime
from typing import List, Union, Dict

from pydantic import BaseModel, validator, Field
from uuid import UUID

from ...Constants.General.GameTypes import GameType, GameTypeDict


class Booster(BaseModel):
    id: str = Field(alias="_id")
    purchaserUUID: UUID = Field(alias="purchaserUuid")
    amount: float
    originalLength: int
    length: int
    gameType: GameType
    stacked: Union[bool, List[UUID]] = False
    dateActivated: datetime

    @validator("gameType", pre=True)
    def populate_gameType(cls: classmethod, gameTypeID: int) -> GameType:
        if gameTypeID in GameTypeDict:
            return GameTypeDict[gameTypeID]
        else:
            return gameTypeID


class Boosters(BaseModel):
    boosters: List[Booster]
    boosterState: bool = False

    @validator("boosterState", pre=True)
    def setDecrementing(cls: classmethod, boosterState: Dict[str, bool]) -> bool:
        if "decrementing" in boosterState:
            return boosterState["decrementing"]
        return False

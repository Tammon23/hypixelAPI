from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, validator


class QuestRewards(BaseModel):
    type: str
    amount: int


class QuestObjectives(BaseModel):
    id: str
    type: str
    integer: Optional[int]


class QuestRequirements(BaseModel):
    type: str


class Quest(BaseModel):
    id: str
    name: str
    rewards: List[QuestRewards]
    objectives: List[QuestObjectives]
    requirements: List[QuestRequirements]
    description: str


class Quests(BaseModel):
    lastUpdated: datetime
    quests: Dict[str, List[Quest]]

    @validator('quests')
    def questsGameUpper(cls: classmethod, quests: Dict[str, Quest]):
        quests_clone = {}

        for game in quests:
            quests_clone[game.upper()] = quests[game]

        return quests_clone

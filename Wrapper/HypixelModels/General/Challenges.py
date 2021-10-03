from datetime import datetime
from typing import Dict, List

from pydantic import BaseModel, validator


class ChallengeRewards(BaseModel):
    type: str
    amount: int


class Challenge(BaseModel):
    id: str
    name: str
    rewards: List[ChallengeRewards]


class Challenges(BaseModel):
    lastUpdated: datetime
    challenges: Dict[str, List[Challenge]]

    @validator('challenges')
    def challengesGameUpper(cls: classmethod, challenges: Dict[str, Challenge]):
        challenges_clone = {}

        for game in challenges:
            challenges_clone[game.upper()] = challenges[game]

        return challenges_clone

from datetime import datetime
from typing import Dict, Any, List

from pydantic import BaseModel


class GuildAchievementReward(BaseModel):
    tier: int
    amount: int


class GuildAchievement(BaseModel):
    name: str
    description: str
    tiers: List[GuildAchievementReward]


class GuildAchievements(BaseModel):
    lastUpdated: datetime
    one_time: Dict[Any, Any]
    tiered: Dict[str, GuildAchievement]

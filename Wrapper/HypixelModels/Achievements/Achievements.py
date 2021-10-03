from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, validator


class OneTimeAchievementInformation(BaseModel):
    points: int
    name: str
    description: str
    gamePercentUnlocked: Optional[float]
    globalPercentUnlocked: Optional[float]
    legacy: bool = False


class AchievementTiers(BaseModel):
    tier: int
    points: int
    amount: int


class TieredAchievementInformation(BaseModel):
    name: str
    description: str
    tiers: List[AchievementTiers]


class Achievement(BaseModel):
    one_time: Dict[str, OneTimeAchievementInformation]
    tiered: Dict[str, TieredAchievementInformation]
    total_points: int
    total_legacy_points: int


class Achievements(BaseModel):
    lastUpdated: datetime
    achievements: Dict[str, Achievement]

    @validator('achievements')
    def achievementGameUpper(cls: classmethod, achievements: Dict[str, Achievement]):
        achievements_clone = {}

        for game in achievements:
            achievements_clone[game.upper()] = achievements[game]

        return achievements_clone

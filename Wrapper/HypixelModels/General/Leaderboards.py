from typing import List, Dict
from uuid import UUID

from pydantic import BaseModel


class Leaderboard(BaseModel):
    path: str
    prefix: str
    title: str
    location: str
    count: int
    leaders: List[UUID]


class Leaderboards(BaseModel):
    leaderboards: Dict[str, List[Leaderboard]]

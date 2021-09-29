from pydantic import BaseModel
from uuid import UUID


class APIKey(BaseModel):
    key: str
    owner: UUID
    limit: int
    queriesInPastMin: str
    totalQueries: int

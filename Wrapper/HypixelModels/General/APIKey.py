from uuid import UUID

from pydantic import BaseModel


class APIKey(BaseModel):
    key: str
    owner: UUID
    limit: int
    queriesInPastMin: str
    totalQueries: int

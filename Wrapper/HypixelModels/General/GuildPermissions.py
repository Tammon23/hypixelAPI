from datetime import datetime
from typing import List, Dict

from pydantic import BaseModel


class GuildPermissionItem(BaseModel):
    name: str


class GuildPermission(BaseModel):
    name: str
    description: str
    item: GuildPermissionItem


class GuildPermissions(BaseModel):
    lastUpdated: datetime
    permissions: List[Dict[str, GuildPermission]]

    def availableLanguages(self):

        languages = set()
        for permission in self.permissions:
            languages.update(permission.keys())

        return languages

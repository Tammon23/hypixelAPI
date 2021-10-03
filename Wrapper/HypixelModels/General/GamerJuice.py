from typing import Dict

from pydantic import BaseModel


class GamerJuice(BaseModel):
    id: int
    databaseName: str
    modeNames: Dict[str, str] = None
    legacy: bool = False

    def getModes(self):
        if self.modeNames is None:
            return None
        return self.modeNames.keys()

import json
from typing import Dict, Any

from milestone_two.utils.dataaccess.database import Database


class FileDatabase(Database):
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)

    def load_database(self) -> Dict[str, Any]:
        db: Dict[str, Any] = {}

        for key in self.config:
            with open(self.config[key], "r", encoding="utf8") as file:
                json_content = json.load(file)
                db[key] = json_content["Results"]

        return db

from typing import Generator

from milestone_two.utils.dataaccess.models.make import Make
from milestone_two.utils.dataaccess.repositories.repository import Repository
from milestone_two.utils.dataaccess.sqlitedatabase.sqlite_database import SQLiteDatabase


class MakesRepository(Repository):
    def __init__(self, db: SQLiteDatabase):
        super().__init__(db)

    def get_makes(self) -> Generator[Make, None, None]:
        q = super().create_select_query("makes", "id", "name", "version")
        results = self.get_entities(q)

        for result in results:
            yield Make(*result)

    def get_make(self, name: str) -> Make:
        q = super().create_select_query("makes", "id", "name", "version", where=f"name = '{name}'", limit=1)
        results = list(self.get_entities(q))

        if len(results) > 0:
            return Make(*results[0])

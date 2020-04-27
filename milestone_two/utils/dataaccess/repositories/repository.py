import abc
from typing import Generator

from milestone_two.utils.dataaccess.sqlitedatabase.sqlite_database import SQLiteDatabase


class Repository(abc.ABC):
    @abc.abstractmethod
    def __init__(self, db: SQLiteDatabase):
        self._db = db

    def get_entities(self, query: str) -> Generator[tuple, None, None]:
        results = self._db.select(query)

        for result in results:
            yield result

    @staticmethod
    def create_select_query(entity: str, *attributes, **behaviors) -> str:
        query = f"SELECT {','.join(attributes)} FROM {entity} "

        if behaviors.get("where") is not None:
            query += f"WHERE {behaviors['where']} "

        if behaviors.get("limit") is not None:
            query += f"LIMIT {int(behaviors['limit'])} "

        return query

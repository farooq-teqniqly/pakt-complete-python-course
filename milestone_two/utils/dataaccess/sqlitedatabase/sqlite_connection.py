import sqlite3 as db
from sqlite3.dbapi2 import Connection


class SQLiteConnection:
    def __init__(self, database_name: str):
        self._connection = None
        self._database_name = database_name

    def __enter__(self) -> Connection:
        self._connection = db.connect(f"{self._database_name}.db")
        return self._connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_val:
            self._connection.commit()

        self._connection.close()

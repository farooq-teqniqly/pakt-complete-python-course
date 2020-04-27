import json
import sqlite3 as db
import time
from typing import Dict, Any, List

from milestone_two.utils.dataaccess.models.make import Make


class SQLiteDatabase:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self._connection = db.connect(f"{config['database_name']}.db")

        cursor = self._connection.cursor()
        cursor.execute(
            """CREATE TABLE makes
                                (
                                    id INTEGER PRIMARY KEY, 
                                    ext_id INTEGER, 
                                    name TEXT, 
                                    version INTEGER, 
                                    date_modified INTEGER
                                )"""
        )

        cursor.execute("CREATE UNIQUE INDEX idx_makes ON makes(name, version)")

        cursor.execute(
            """CREATE TABLE vehicle_variables
                            (
                                id INTEGER PRIMARY KEY, 
                                ext_id INTEGER, 
                                name TEXT, 
                                description TEXT, 
                                data_type TEXT,
                                date_modified INTEGER
                            )"""
        )

        cursor.execute("CREATE UNIQUE INDEX idx_vehicle_variables ON vehicle_variables(name)")
        self._connection.commit()

    def load_database(self) -> Dict[str, Any]:
        with open(self.config["makes"], "r", encoding="utf8") as makes_file:
            makes_json = json.load(makes_file)

        for make in makes_json["Results"]:
            cursor = self._connection.cursor()
            values = (make['Make_ID'], make['Make_Name'], 1, int(time.time()))

            cursor.execute(
                f"INSERT INTO makes (ext_id, name, version, date_modified) VALUES (?, ?, ?, ?)",
                values
            )

        self._connection.commit()

        with open(self.config["vehicle_variables"], "r", encoding="utf8") as vehicle_variables_file:
            vehicle_variables_json = json.load(vehicle_variables_file)

        for vehicle_variable in vehicle_variables_json["Results"]:
            cursor = self._connection.cursor()
            values = (
                vehicle_variable['ID'],
                vehicle_variable['Name'],
                vehicle_variable['Description'],
                vehicle_variable['DataType'],
                int(time.time()))

            cursor.execute(
                f"""INSERT INTO vehicle_variables (ext_id, name, description, data_type, date_modified) 
                    VALUES (?, ?, ?, ?, ?)""",
                values
            )

        self._connection.commit()

    def upsert_make(self, make: Make) -> Make:
        pass

    def select(self, query: str) -> List[tuple]:
        cursor = self._connection.cursor()
        cursor.execute(query)

        return cursor.fetchall()

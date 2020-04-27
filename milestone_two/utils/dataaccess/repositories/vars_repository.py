from typing import Generator

from milestone_two.utils.dataaccess.models.vehicle_variable import VehicleVariable
from milestone_two.utils.dataaccess.repositories.repository import Repository
from milestone_two.utils.dataaccess.sqlitedatabase.sqlite_database import SQLiteDatabase


class VarsRepository(Repository):
    def __init__(self, db: SQLiteDatabase):
        super().__init__(db)

    def get_vars(self) -> Generator[VehicleVariable, None, None]:
        q = super().create_select_query("vehicle_variables", "id", "name")
        results = self.get_entities(q)

        for result in results:
            yield VehicleVariable(*result)

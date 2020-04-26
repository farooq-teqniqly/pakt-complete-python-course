import json
from typing import Dict, Any

from milestone_two.utils.dataaccess.database import Database
from milestone_two.utils.dataaccess.models.make import Make
from milestone_two.utils.dataaccess.models.vehicle_variable import VehicleVariable


class FileDatabase(Database):

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)

    def upsert_make(self, name: str) -> Make:
        makes = list(self.find_make(name))
        make: Make

        if makes is not None:
            makes.sort(key=lambda m: m.version, reverse=True)
            make = Make(makes[0].id + 1000, name, makes[0].version + 1)
            self.data["makes"].add(make)
        else:
            make = Make(1000, name)
            self.data["makes"].add(make)

        return make

    def load_database(self) -> Dict[str, Any]:
        db: Dict[str, set] = {}

        makes_json = FileDatabase._load_file(self.config["makes"])
        makes = set()

        for make in makes_json["Results"]:
            makes.add(Make(make["Make_ID"], make["Make_Name"]))

        db["makes"] = makes

        vehicle_variables_json = FileDatabase._load_file(self.config["vehicle_variables"])
        vehicle_variables = set()

        for vehicle_variable in vehicle_variables_json["Results"]:
            vehicle_variables.add(VehicleVariable(vehicle_variable["ID"], vehicle_variable["Name"]))

        db["vehicle_variables"] = vehicle_variables

        return db

    @staticmethod
    def _load_file(path) -> dict:
        with open(path, "r", encoding="utf8") as file:
            return json.load(file)

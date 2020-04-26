from typing import List

from milestone_two.utils.dataaccess.filedatabase.file_database import FileDatabase
from milestone_two.utils.dataaccess.models.make import Make
from milestone_two.utils.dataaccess.models.vehicle_variable import VehicleVariable

USAGE = """
    - 'l' to list all makes
    - 'v' to list vehicle variables
    - 'q' to quit
"""


def list_makes(db: FileDatabase) -> List[Make]:
    return list(db.get_makes())


def list_vehicle_variables(db: FileDatabase) -> List[VehicleVariable]:
    return list(db.get_vehicle_variables())


def run(db: FileDatabase):
    while True:
        user_input = input(USAGE)

        if user_input.lower() == "q":
            exit(0)

        if user_input.lower() == "l":
            print(list_makes(db))
        elif user_input.lower() == "v":
            print(list_vehicle_variables(db))
        else:
            print(USAGE)


if __name__ == "__main__":
    run(FileDatabase(
        {
            "makes": "utils/dataaccess/filedatabase/seed_data/vehicle_makes.json",
            "vehicle_variables": "utils/dataaccess/filedatabase/seed_data/vehicle_variables.json"
         }
    ))

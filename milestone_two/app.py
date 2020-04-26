from typing import List

from milestone_two.utils.dataaccess.filedatabase.file_database import FileDatabase
from milestone_two.utils.dataaccess.models.make import Make
from milestone_two.utils.dataaccess.models.vehicle_variable import VehicleVariable

USAGE = """
    - 'l' to list all makes
    - 'um' to update/insert makes
    - 'v' to list vehicle variables
    - 'q' to quit
"""


def list_makes(db: FileDatabase) -> List[Make]:
    return list(db.get_makes())


def update_make(db: FileDatabase, name: str) -> Make:
    return db.upsert_make(name)


def update_make(db: FileDatabase, name: str) -> Make:
    return db.upsert_make(name)


def remove_make(db: FileDatabase, name: str, version: int) -> Make:
    return db.remove_make(name, version)


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
        elif user_input.lower() == "um":
            make_to_update_name = input("Enter the name of the make: ")
            print(update_make(db, make_to_update_name))
        elif user_input.lower() == "rm":
            make_to_remove_name = input("Enter the name of the make: ")
            make_to_remove_version = input("Enter the version number: ")
            print(remove_make(db, make_to_remove_name, int(make_to_remove_version)))
        else:
            print(USAGE)


if __name__ == "__main__":
    run(FileDatabase(
        {
            "makes": "utils/dataaccess/filedatabase/seed_data/vehicle_makes.json",
            "vehicle_variables": "utils/dataaccess/filedatabase/seed_data/vehicle_variables.json"
         }
    ))

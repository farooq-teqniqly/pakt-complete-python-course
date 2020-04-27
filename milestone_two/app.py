import os
from typing import List

from milestone_two.utils.dataaccess.models.make import Make
from milestone_two.utils.dataaccess.models.vehicle_variable import VehicleVariable
from milestone_two.utils.dataaccess.repositories.makes_repository import MakesRepository
from milestone_two.utils.dataaccess.repositories.vars_repository import VarsRepository
from milestone_two.utils.dataaccess.sqlitedatabase.sqlite_database import SQLiteDatabase

USAGE = """
    - 'makes list' to list all makes
    - 'makes show' to show a particular make
    - 'vars list' to list vehicle variables
    - 'q' to quit
"""


def list_makes(repo: MakesRepository) -> List[Make]:
    return list(repo.get_makes())


def list_make(repo: MakesRepository, name: str):
    return repo.get_make(name)


def list_vehicle_variables(repo: VarsRepository) -> List[VehicleVariable]:
    return list(repo.get_vars())


def run(**repos):
    while True:
        user_input = input(USAGE)

        if user_input.lower() == "q":
            exit(0)

        if user_input.lower() == "makes list":
            print(list_makes(repos["makes"]))
        elif user_input.lower() == "vars list":
            print(list_vehicle_variables(repos["vars"]))
        elif user_input.lower() == "makes show":
            make_name = input("Enter a make name: ")
            print(list_make(repos["makes"], make_name))
        else:
            print(USAGE)


if __name__ == "__main__":
    database_name = "foo"

    os.remove(f"{database_name}.db")

    db = SQLiteDatabase(
        {
            "database_name": database_name,
            "makes": "utils/dataaccess/sqlitedatabase/seed_data/vehicle_makes.json",
            "vehicle_variables": "utils/dataaccess/sqlitedatabase/seed_data/vehicle_variables.json"
        }
    )

    db.load_database()

    repositories = {
        "makes": MakesRepository(db),
        "vars": VarsRepository(db)
    }

    run(**repositories)

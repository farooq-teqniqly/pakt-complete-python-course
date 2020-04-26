from typing import List

from milestone_two.utils.database import FileDatabase, Make

USAGE = """
    - 'l' to list all makes
    - 'q' to quit
"""


def list_makes(db: FileDatabase) -> List[Make]:
    return list(db.get_makes())


def run(db: FileDatabase):
    while True:
        user_input = input(USAGE)

        if user_input.lower() == "q":
            exit(0)

        if user_input.lower() == "l":
            print(list_makes(db))
        else:
            print(USAGE)


if __name__ == "__main__":
    run(FileDatabase({"makes": "../file_lesson/vehicle_makes.json"}))

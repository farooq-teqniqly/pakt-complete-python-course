from collections import namedtuple
from typing import List

if __name__ == "__main__":
    data = [
        {"make": "Ford", "model": "Edge"},
        {"make": "Ford", "model": "Mustang"},
        {"make": "Ford", "model": "Ranger"}
    ]

    Vehicle = namedtuple("Vehicle", ["make", "model"])

    vehicles: List[Vehicle] = []

    for item in data:
        vehicles.append(Vehicle(**item))

    for v in vehicles:
        print(v)
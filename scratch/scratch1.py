from typing import List
from pprint import pprint as pp


class Vehicle:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def __str__(self) -> str:
        return f"{self.make} {self.model}"


class Garage:
    def __init__(self, vehicles: List[Vehicle]):
        self.vehicles = vehicles

    def __len__(self) -> int:
        return len(self.vehicles)

    def __getitem__(self, key: int) -> Vehicle:
        return self.vehicles[key]

    def __str__(self) -> str:
        return str(self.vehicles)


if __name__ == "__main__":
    edge = Vehicle("Ford", "Edge")
    mustang = Vehicle("Ford", "Mustang")
    ranger = Vehicle("Ford", "Ranger")

    garage = Garage([edge, mustang, ranger])

    print(len(garage))

    print(garage[2])

    for _, v in enumerate(garage):
        print(v)

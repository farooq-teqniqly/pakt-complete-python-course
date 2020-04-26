import abc

from typing import Generator, Dict, Any
from milestone_two.utils.dataaccess.models.make import Make
from milestone_two.utils.dataaccess.models.vehicle_variable import VehicleVariable


class Database(abc.ABC):
    @abc.abstractmethod
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.data = self.load_database()
        pass

    @abc.abstractmethod
    def load_database(self) -> Dict[str, Any]:
        pass

    def get_makes(self) -> Generator[Make, None, None]:
        for make in self.data["makes"]:
            yield make

    def find_make(self, name: str, **kwargs) -> Generator[Make, None, None]:
        find_version: int = kwargs.get("find_version")

        for make in self.data["makes"]:
            if make.name == name:
                if find_version is not None:
                    if make.version == find_version:
                        yield make
                else:
                    yield make

    def remove_make(self, name: str, version: int) -> Make:
        make = list(self.find_make(name, find_version=version))[0]
        self.data["makes"].remove(make)
        return make

    @abc.abstractmethod
    def upsert_make(self, make: Make) -> Make:
        pass

    def get_vehicle_variables(self) -> Generator[VehicleVariable, None, None]:
        for vehicle_variable in self.data["vehicle_variables"]:
            yield vehicle_variable

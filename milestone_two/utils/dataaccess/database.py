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
            yield Make(make["Make_ID"], make["Make_Name"])

    def get_vehicle_variables(self) -> Generator[VehicleVariable, None, None]:
        for v in self.data["vehicle_variables"]:
            yield VehicleVariable(v["ID"], v["Name"])


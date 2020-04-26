import abc
import json

from typing import Generator, Dict, Any


class Make:
    def __init__(self, make_id: int, name: str):
        self._id = make_id
        self._name = name

    def __repr__(self) -> str:
        return f"({self.id}, {self._name})"

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name


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


class FileDatabase(Database):
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)

    def load_database(self) -> Dict[str, Any]:
        db: Dict[str, Any] = {}

        for key in self.config:
            with open(self.config[key], "r") as file:
                json_content = json.load(file)
                db[key] = json_content["Results"]

        return db

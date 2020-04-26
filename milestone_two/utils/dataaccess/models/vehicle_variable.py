class VehicleVariable:
    def __init__(self, var_id: int, name: str):
        self._var_id = var_id
        self._name = name

    def __repr__(self) -> str:
        return f"({self.id}, {self.name})"

    @property
    def id(self) -> int:
        return self._var_id

    @property
    def name(self) -> str:
        return self._name

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

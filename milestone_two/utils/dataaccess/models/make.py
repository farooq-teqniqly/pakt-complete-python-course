class Make:
    def __init__(self, make_id: int, name: str, version: int = 1):
        self._id = make_id
        self._name = name
        self._version = version

    def __repr__(self) -> str:
        return f"({self.id}, {self._name}, {self._version})"

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def version(self) -> int:
        return self._version

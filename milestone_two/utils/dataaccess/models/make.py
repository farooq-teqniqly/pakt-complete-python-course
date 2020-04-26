class Make:
    def __init__(self, make_id: int, name: str, version: int = 1):
        self._id = make_id
        self._name = name
        self._version = version

    def __repr__(self) -> str:
        return f"({self.id}, {self._name}, {self._version})"

    def __eq__(self, other):
        return (self._name.lower() == other.name.lower()) and (self._version == other.version)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self._name.lower()) ^ hash(self._version)

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def version(self) -> int:
        return self._version

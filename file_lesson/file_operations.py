def save(content: str, path: str) -> None:
    with open(path, "w") as writer:
        writer.write(content)


def read_as_string(path: str) -> str:
    with open(path, "r") as reader:
        return reader.read()

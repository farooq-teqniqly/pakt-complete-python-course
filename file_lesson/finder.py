from typing import Callable, Any


class NotFoundError(Exception):
    pass


def find_in(iterable, predicate: Callable[[Any], bool]) -> int:
    for index, item in enumerate(iterable):
        if predicate(item):
            return index

    raise NotFoundError(f"No elements matched.")


if __name__ == "__main__":
    items = ["Bubba", "Gump", "shrimp"]
    print(find_in(items, lambda i: i == "Gump"))
    print(find_in(items, lambda i: i == "Foo"))
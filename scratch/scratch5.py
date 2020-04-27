from typing import Tuple


def add(*numbers: Tuple[int]) -> int:
    return sum(numbers)


if __name__ == "__main__":
    values = range(1, 101)
    print(add(*values))
    print(sum(range(1, 101)))
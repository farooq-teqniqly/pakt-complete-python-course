"""
This is an iterator.
"""


class FirstNGenerator:
    def __init__(self, max_num: int):
        self._max_num = max_num;
        self._current_num = 0

    def __next__(self):
        if self._current_num < self._max_num:
            save = self._current_num
            self._current_num += 1
            return save
        else:
            raise StopIteration()

    def __iter__(self):
        return self


if __name__ == "__main__":
    g = FirstNGenerator(100)

    # Below is a generator comprehension
    g2 = (x for x in g if x % 5 == 0)

    print(list(g2))

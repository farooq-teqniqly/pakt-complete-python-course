from collections import namedtuple

PrintJobReport = namedtuple("PrintJobReport", ["pages", "pages_per_second", "pages_remaining"])


class PrinterError(RuntimeError):
    pass


class Printer:
    def __init__(self, capacity: int, pages_per_second: float):
        self._capacity = capacity
        self._pages_per_second = pages_per_second

    @property
    def remaining_capacity(self) -> int:
        return self._capacity

    def print(self, pages: int) -> PrintJobReport:
        if pages > self._capacity:
            raise PrinterError("PC Load Letter")

        self._capacity -= pages

        return PrintJobReport(pages, round(pages / self._pages_per_second, 1), self._capacity)

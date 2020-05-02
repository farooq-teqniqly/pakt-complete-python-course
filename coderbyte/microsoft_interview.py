"""
Module with various Microsoft interview coding exercises.
Exercises obtained from https://www.coderbyte.com/course/microsoft-interview-questions.
"""
from typing import Generator, List


def find_duplicates(values: List[int]) -> Generator[int, None, None]:
    """
    Finds duplicates using the following algorithm:

    For each element in the array:
        Get the value of array[abs(array[index])]
        If the value is positive, make it negative.
        If the value is negative it is a duplicate -> return the number.

    It is assumed that the array values are between 0 and len(array) - 1 inclusive.

    Args:
        *values (List[int]): The array to check.

    Returns:
        A generator for the duplicate numbers.
    """
    for index, value in enumerate(values):
        check_index = abs(values[index])
        check = values[check_index]

        if check < 0:
            yield abs(value)
        else:
            values[check_index] *= -1


for dupe in list(find_duplicates([1, 1, 4, 2, 3, 3, 4, 1, 4])):
    print(dupe)

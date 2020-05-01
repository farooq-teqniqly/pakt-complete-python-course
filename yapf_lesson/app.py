from typing import Union

vehicles = ["Edge", "Mustang", "Ranger", "Explorer"]

for vehicle in vehicles:
    print(vehicle)

print("We're done!")


def add(*values: Union[int, float]) -> Union[int, float]:
    """
    Args:
        *values (int): The values to add.
    Returns:
        int: The result
    """

    result = 0

    for v in values:
        result += v

    return result


z = add(2, 3, 4, 5)
print(z)

z = add(3.1, 2, 4.555, 1, 11.86)

print(z)

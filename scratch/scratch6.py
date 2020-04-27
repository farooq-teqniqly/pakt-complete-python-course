from collections import Counter, defaultdict


def default_dict_example():
    dealer_locations = [("Mercedes-Benz", "Canada"),
                        ("Mercedes-Benz", "United States"),
                        ("Tesla", "United States")]

    dealer_locations_dict = defaultdict(list)

    for make, location in dealer_locations:
        dealer_locations_dict[make].append(location)

    print(dealer_locations_dict["Mercedes-Benz"])
    print(dealer_locations_dict["Tesla"])
    print(dealer_locations_dict["Ford"])


def default_dict_example2():
    data = [
                {"name": "Bubba", "version": 1},
                {"name": "Stan", "version": 2}
            ]

    updated_versions = defaultdict(int)

    for _, item in enumerate(data):
        updated_versions.update({item["name"]: item["version"] + 1})

    print(updated_versions["Bubba"])
    print(updated_versions["Stan"])
    print(updated_versions["Hugh"])


def counter_example():
    multiples_of_ten = (x for x in range(1, 101) if x % 10 == 0)
    counter = Counter(multiples_of_ten)
    print(counter)


if __name__ == "__main__":
    default_dict_example2()

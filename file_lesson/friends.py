from typing import Generator, AbstractSet


def clean_string(s: str) -> str:
    return s.strip()


def find_nearby_friends(friends: AbstractSet[str]) -> Generator[str, None, None]:

    with open("people.txt", "r") as read_file:
        nearby_friends: AbstractSet[str] = set(read_file.read().splitlines())

    for _, friend in enumerate(friends):
        if clean_string(friend) in nearby_friends:
            yield friend


if __name__ == "__main__":
    friends_input = input("Enter up to three friends. Separate multiple friends by a comma: ")
    results = set(clean_string(nearby_friend) for nearby_friend in find_nearby_friends(friends_input.split(",")))

    if results:
        with open("nearby_friends.txt", "w") as write_file:
            write_file.writelines(f"{clean_string(result)}\n" for result in results)

    print(f"Nearby friends: {results}")

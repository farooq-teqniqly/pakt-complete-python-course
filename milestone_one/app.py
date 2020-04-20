"""
Enter 'a' to add a movie.
Enter 'l' to list movies.
Enter 'f' to find a movie.
Enter 'r' to remove a movie.
Enter 'q' to quit.
"""

movie_list: [list] = []

USAGE: [str] = """Enter 'a' to add a movie.
    Enter 'l' to list movies.
    Enter 'f' to find a movie.
    Enter 'r' to remove a movie.
    Enter 'q' to quit."""


def list_movies() -> str:
    return movie_list


def find_movie(title: str) -> list:
    return list(filter(lambda t: compare_strings_safe(t, title), movie_list))


def add_movie(title: [str]) -> None:
    movie_list.append(title)


def remove_movie(title: str) -> None:
    for index, movie in enumerate(movie_list):
        if compare_strings_safe(title, movie):
            del movie_list[index]


def compare_strings_safe(s1: str, s2: str) -> bool:
    return s1.casefold() == s2.casefold()


def run():
    print(USAGE)

    while True:
        user_input: str = input()

        if compare_strings_safe(user_input, "q"):
            print("Goodbye.")
            break

        elif compare_strings_safe(user_input, "l"):
            print(list_movies())

        elif compare_strings_safe(user_input, "f"):
            title: str = input("Movie title: ")
            print(find_movie(title))

        elif compare_strings_safe(user_input, "a"):
            title: str = input("Movie title: ")
            add_movie(title)
            print(f"Movie '{title}' added.")

        elif compare_strings_safe(user_input, "r"):
            title: str = input("Movie title: ")
            remove_movie(title)
            print(f"Movie '{title}' removed.")

        else:
            print(USAGE)


if __name__ == "__main__":
    run()

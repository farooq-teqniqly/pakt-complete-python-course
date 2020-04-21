from typing import List
from movie import Movie

"""
Enter 'a' to add a movie.
Enter 'l' to list movies.
Enter 'f' to find a movie.
Enter 'r' to remove a movie.
Enter 'q' to quit.
"""

movie_list: List[Movie] = []

USAGE: str = """Enter 'a' to add a movie.
    Enter 'l' to list movies.
    Enter 'f' to find a movie.
    Enter 'r' to remove a movie.
    Enter 'q' to quit."""


def list_movies() -> List[Movie]:
    return movie_list


def find_movie_by_title(title: str) -> List[Movie]:
    return list(filter(lambda t: compare_strings_safe(t.title, title), movie_list))


def add_movie(movie: Movie) -> None:
    movie_list.append(movie)


def remove_movie(title: str) -> None:
    for index, movie in enumerate(movie_list):
        if compare_strings_safe(title, movie.title):
            del movie_list[index]


def compare_strings_safe(s1: str, s2: str) -> bool:
    return s1.casefold() == s2.casefold()


def run():
    print(USAGE)

    while True:
        user_input: str = input()

        if compare_strings_safe(user_input, "q"):
            print("Goodbye.")

        elif compare_strings_safe(user_input, "l"):
            movies = list_movies()

            if not movies:
                print("No movies.")
            else:
                for movie in list_movies():
                    print(movie)

        elif compare_strings_safe(user_input, "f"):
            title: str = input("Movie title: ")

            for movie in find_movie_by_title(title):
                print(movie)

        elif compare_strings_safe(user_input, "a"):

            movie_data = []

            while len(movie_data) < 3:
                title: str = input("Enter the movie's title, director, and release date as a comma separated list: ")
                movie_data = title.split(",")

            add_movie(Movie(movie_data[0], movie_data[1], movie_data[2]))
            print(f"Movie '{title}' added.")

        elif compare_strings_safe(user_input, "r"):
            title: str = input("Movie title: ")
            remove_movie(title)
            print(f"Movie '{title}' removed.")

        else:
            print(USAGE)


if __name__ == "__main__":
    run()

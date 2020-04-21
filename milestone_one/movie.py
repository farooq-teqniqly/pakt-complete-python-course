from datetime import date
import jsonpickle


class Movie:
    def __init__(self, title: str, director: str, release_date: date):
        self.title = title
        self.director = director
        self.release_date = release_date

    def json(self):
        return jsonpickle.encode(self)

    def __str__(self):
        return self.json()

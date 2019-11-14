from database import Database
from movies.movies import Movie
from readfromfiles.read_data_from_file import ReadMoviesFromTxt


class MovieDatabase(Database):

    def __init__(self):
        self.database = dict()
        self.list_of_titles = []
        ReadMoviesFromTxt(self).read_movies()

    def add_to_database(self, new_object):
        if not isinstance(new_object, Movie):
            raise ValueError("This is not a movie! You cannot add it to movie database!")
        if new_object.get_title() not in self.list_of_titles:
            self.database[new_object.get_title()] = new_object
            self.list_of_titles.append(new_object.get_title())
            self.list_of_titles.sort()

    def remove_from_database(self, existing_object):
        pass

    def look_for(self, object):
        pass

    def print_database_content(self):
        for movie in self.list_of_titles:
            print(movie)

    def get_database(self):
        return self.database.values()




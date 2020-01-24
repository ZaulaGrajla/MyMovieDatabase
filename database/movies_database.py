from database import Database
from movies.movies import Movie
from readfromfiles.read_data_from_file import ReadFromTxt


class MovieDatabase(Database):

    def __init__(self):
        self.database = dict()
        self.list_of_titles = []
        ReadFromTxt(self, '\\movies.txt', Movie).read_data()

    def add_to_database(self, new_object):
        if not isinstance(new_object, Movie):
            raise ValueError("This is not a movie! You cannot add it to movie database!")
        if new_object.get_title() not in self.list_of_titles:
            self.database[new_object.get_title()] = new_object
            self.list_of_titles.append(new_object.get_title())
            self.list_of_titles.sort()

    def remove_from_database(self, existing_object):
        pass

    def look_for(self, obj):
        pass

    def print_database_content(self):
        letters = []
        for movie in self.list_of_titles:
            letter = movie[0].upper()
            if letter not in letters:
                print(letter)
                letters.append(letter)
            print(movie)

    def get_database(self):
        return self.database.values()





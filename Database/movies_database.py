from Database.database import Database
from movies.movies import Movie


class MovieDatabase(Database):

    def __init__(self):
        self.database = {}
        self.list_of_titles=[]

    def add_to_database(self, new_object):
        if not isinstance(new_object, Movie):
            raise ValueError("This is not a movie! You cannot add it to movie database!")
        self.database[new_object.get_title()]=new_object
        self.list_of_titles.append(new_object.get_title())
        self.list_of_titles.sort()


    def remove_from_database(self, existing_object):
        pass

    def look_for_title(self, existing_object):
        pass

    def look_for_year(self, existing_object):
        pass

    def look_for_actor(self, existing_object):
        pass

    def print_database_content(self):
        for movie in self.list_of_titles:
            print(movie)

baza=MovieDatabase()
baza.add_to_database(Movie("Władca pierścieni",2000))
baza.add_to_database(Movie("Harry Potter",2001))
baza.add_to_database(Movie("Roger",2009))
baza.print_database_content()
import os

from movies_database import MovieDatabase
from movies.movies import Movie


class ReadMoviesFromTxt():

    def __init__(self, name_of_file='\\movies.txt'):
        self.file = self.get_path()
        self.file_to_read_name = name_of_file
        self.movie_database_from_file = MovieDatabase()

    def get_path(self):
        return os.path.abspath(os.path.dirname(__file__))

    def read_movies(self):

        with open(f'{self.get_path()}{self.file_to_read_name}', 'r') as file:
            movie_data = file.readline().split(",")
            while not (movie_data == [] or movie_data == ['\n']):
                for element in range(len(movie_data)):
                    movie_data[element] = movie_data[element].strip()
                self.movie_database_from_file.add_to_database(Movie(movie_data[0], movie_data[1], movie_data[2]))
                movie_data = file.readline().split(",")
            self.movie_database_from_file.print_database_content()

ReadMoviesFromTxt().read_movies()
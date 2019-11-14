import os

from actors.actors import Actor
from movies.movies import Movie


class ReadMoviesFromTxt():

    def __init__(self, movie_database, name_of_file='\\movies.txt'):
        self.file = self.get_path()
        self.file_to_read_name = name_of_file
        self.movie_database_from_file = movie_database

    def get_path(self):
        return os.path.abspath(os.path.dirname(__file__))

    def read_movies(self):
        with open(f'{self.get_path()}{self.file_to_read_name}', 'r') as file:
            movie_data = file.readline().split(",")
            while "End of the list" not in movie_data:
                for element in range(len(movie_data)):
                    movie_data[element] = movie_data[element].strip()
                self.movie_database_from_file.add_to_database(Movie(movie_data[0], movie_data[1], movie_data[2]))
                movie_data = file.readline().split(",")



class ReadActorsFromTxt():

    def __init__(self, actors_database, name_of_file='\\actors.txt'):
        self.file = self.get_path()
        self.file_to_read_name = name_of_file
        self.actors_from_file = actors_database

    def get_path(self):
        return os.path.abspath(os.path.dirname(__file__))

    def read_actors(self):
        with open(f'{self.get_path()}{self.file_to_read_name}', 'r') as file:
            actors_data = file.readline().split(",")
            while "End of the list" not in actors_data:
                if '\n' in actors_data:
                    actors_data.remove('\n')
                for element in range(len(actors_data)):
                    actors_data[element] = actors_data[element].strip()
                self.actors_from_file.add_to_database(Actor(*actors_data))
                actors_data = file.readline().split(",")



class ReadCastFromTxt():

    def __init__(self, name_of_file='\\cast.txt'):
        self.file = self.get_path()
        self.file_to_read_name = name_of_file

    def get_path(self):
        return os.path.abspath(os.path.dirname(__file__))

    def read_cast(self, movie_database, actors_database):
        with open(f'{self.get_path()}{self.file_to_read_name}', 'r') as file:
            cast_data = file.readline().split(",")
            while "End of the list" not in cast_data:
                if '\n' in cast_data:
                    cast_data.remove('\n')
                for element in range(len(cast_data)):
                    cast_data[element] = cast_data[element].strip()

                title = cast_data[0]
                if title in movie_database.list_of_titles:
                    movie_object = movie_database.database[title]
                    cast_members = len(cast_data)
                    for cast in range(1, cast_members):
                        actor_name, role = cast_data[cast].split(" as ")[0], cast_data[cast].split(" as ")[1]
                        if actor_name in actors_database.list_of_actors:
                            actor = actors_database.database[actor_name]
                            movie_object.add_cast(actor, role)

                cast_data = file.readline().split(",")



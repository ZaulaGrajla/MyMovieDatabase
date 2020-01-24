import os

class ReadFromTxt:
    """This class can serve both actor and movie database"""

    def __init__(self, database, name_of_file, class_type):
        self.file = self.get_path()
        self.file_to_read_name = name_of_file
        self.database_from_file = database
        self.class_type = class_type

    @staticmethod
    def get_path():
        return os.path.abspath(os.path.dirname(__file__))

    def read_data(self):
        with open(f'{self.get_path()}{self.file_to_read_name}', 'r') as file:
            data = [i.strip() for i in file.readline().split(",") if i.strip() != '']
            while data:
                self.database_from_file.add_to_database(self.class_type(*data))
                data = [i.strip() for i in file.readline().split(",") if i.strip() != '']


class ReadCastFromTxt:

    def __init__(self, name_of_file='\\cast.txt'):
        self.file = self.get_path()
        self.file_to_read_name = name_of_file

    @staticmethod
    def get_path():
        return os.path.abspath(os.path.dirname(__file__))

    def read_cast(self, movie_database, actors_database):
        with open(f'{self.get_path()}{self.file_to_read_name}', 'r') as file:
            cast_data = [i.strip() for i in file.readline().split(",") if i.strip() != '']
            while cast_data:
                title = cast_data[0]
                if title in movie_database.list_of_titles:
                    movie_object = movie_database.database[title]
                    for cast in range(1, len(cast_data)):
                        actor_name, role = cast_data[cast].split(" as ")[0], cast_data[cast].split(" as ")[1]
                        if actor_name in actors_database.list_of_actors:
                            actor = actors_database.database[actor_name]
                            movie_object.add_cast(actor, role)
                cast_data = [i.strip() for i in file.readline().split(",") if i.strip() != '']

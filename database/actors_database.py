from actors import Actor
from database import Database
from readfromfiles.read_data_from_file import ReadFromTxt


class ActorsDatabase(Database):
    def __init__(self):
        self.database = dict()
        self.list_of_actors = []
        ReadFromTxt(self, '\\actors.txt', Actor).read_data()

    def add_to_database(self, actor):
        if not isinstance(actor, Actor):
            raise ValueError("You can add only actors and actresses to database!")
        if actor.get_name() not in self.list_of_actors:
            self.database[actor.get_name()] = actor
            self.list_of_actors.append(actor.get_name())
            self.list_of_actors.sort()

    def print_database_content(self):
        for actor in self.list_of_actors:
            print(actor)

    def get_database(self):
        return self.database.values()

    def remove_from_database(self, existing_object):
        pass

    def look_for(self, obj):
        pass



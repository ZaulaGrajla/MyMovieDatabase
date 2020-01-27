import datetime
import re
import string
import time
from builtins import staticmethod

from actors import Actor
from database import MovieDatabase
from database.actors_database import ActorsDatabase
from movies import Movie
from readfromfiles.read_data_from_file import ReadCastFromTxt, ReadFromTxt
from tools import line_printer


class MovieApplication:

    def __init__(self):
        self.my_movies = MovieDatabase()
        self.my_actors = ActorsDatabase()
        ReadCastFromTxt().read_cast(self.my_movies, self.my_actors)
        self.options = {
            '0': self.exit_app,
            '1': self.show_all_my_movies,
            '2': self.show_all_my_actors,
            '3': self.show_all_my_movies_with_cast,
            '4': self.show_actor_filmography,
            '5': self.show_movie_info,
            '6': self.add_movie_to_database,
            '7': self.add_actor_to_database,
            '8': self.add_cast_to_movie
        }
        self.intro()

    def add_actor_to_database(self):
        sex = self.get_spec_str_from_user(['m', 'w'],
                                          "if this is an actor or an actress?\nPress 1 for man, 2 for woman",
                                          print_option=False)
        name = self.get_str_from_user(question="Please enter first name:\n", duplicate=True).capitalize()
        last_name = self.get_str_from_user(question="Please enter last name:\n", duplicate=True).capitalize()
        if self.check_if_in_db(name + ' ' + last_name, self.my_actors.list_of_actors):
            print("This person already exists in database! Please enter actor's data once again.\n")
            self.add_actor_to_database()
        country = self.get_str_from_user(question="Please enter country in which this person was born:\n",
                                         duplicate=True)
        b_year = self.get_year_from_user("year of birth", 1850)
        d_year = None
        if input("Is this person dead? Press y for yes, press any other key for no.\n") == 'y':
            d_year = self.get_year_from_user("year of death", b_year)
        line_printer.line()
        print("Name:", name, last_name, "\nCountry:", country, "\nYear of birth:", b_year)
        if d_year:
            print("Year of death:", d_year)
        line_printer.line()
        self.add_data_valid('actors', [name, last_name, b_year, country, sex, d_year], self.my_actors, Actor)
        self.add_actor_to_database()

    def add_data_valid(self, db_txt: str, data: list, db_name, class_type):
        validation = input(
            "Are you sure you want to add this person to database?\ny for yes\nn for no\nc for correct data\n")
        if validation == "y":
            self.add_to_txt_database(db_txt, data)
            db_name.add_to_database(class_type(*data))
        elif validation == "c":
            return
        self.intro()

    def add_movie_to_database(self):
        title = self.get_str_from_user("Please enter title of the movie.\n", "movie", "title of movie",
                                       self.my_movies.list_of_titles)
        genre = self.get_spec_str_from_user(Movie.MOVIE_TYPES, "a type of movie")
        year = self.get_year_from_user("year of production", 1899)
        line_printer.line()
        print("Title:", title, "\nType:", genre, "\nYear of production:", year)
        line_printer.line()
        validation = input(
            "Are you sure you want to add such movie to database?\ny for yes\nn for no\nc for correct data\n")
        if validation == "y":
            self.add_to_txt_database('movies', [title, genre, year])
            self.my_movies.add_to_database(Movie(title, genre, year))
        elif validation == "c":
            self.add_movie_to_database()
        else:
            self.intro()

    @staticmethod
    def add_to_txt_database(txt_file: str, data: list, without_new_line=False):
        while None in data:
            data.remove(None)
        with open(f'readfromfiles\\{txt_file}.txt', 'a+') as f:
            f.read()
            if not without_new_line:
                f.write('\n')
            for info in range(len(data)):
                f.write(f'{data[info]},')

    def get_str_from_user(self, question, text1='?', text2='?', database=[], duplicate=False):
        data = input(question).capitalize()
        while not duplicate and self.check_if_in_db(data, database):
            data = input(f"This {text1} exists already in database!\nEnter another {text2}.\n").capitalize()
        return data

    @staticmethod
    def check_if_in_db(data: str, db):
        return True if data.lower() in [i.lower() for i in db] else False

    @staticmethod
    def get_spec_str_from_user(list_to_choose, options: str, print_option=True):
        if print_option:
            for ind, typ in enumerate(list_to_choose):
                print(ind + 1, typ)
        option = 0
        while option not in range(1, len(list_to_choose) + 1):
            try:
                option = int(input(f"Please choose {options}.\n"))
            except ValueError:
                continue
        return list_to_choose[option - 1]

    @staticmethod
    def get_year_from_user(text1, year_to_compare=None):
        year = 0
        while 1900 > year or year > int(datetime.datetime.strftime(datetime.datetime.now(), "%Y")):
            try:
                year = int(input(f"Please enter {text1}.\n"))
                if year_to_compare:
                    if year < year_to_compare:
                        print(f"This year cannot be former than {year_to_compare}")
                        year = 0
            except ValueError:
                continue
        return year

    def add_cast_to_movie(self):
        self.print_with_nl("Warning! Actors and movies that you enter here as cast must already exist in database.\n")
        movie_title = self.look_for("title of movie", self.my_movies.list_of_titles, "no movie titled",
                                    "correct title of movie.",
                                    "Press 1 to return to menu and add new movie to database.")
        cast = []
        while movie_title:
            actor_name = self.look_for("name of actor/actress", self.my_actors.list_of_actors, "no such person",
                                       "correct name of actor/actress.",
                                       "Press 1 to return to menu and add new actor/actress to database.")
            if actor_name in [actor.get_name() for actor in self.my_movies.database[movie_title].cast.cast.keys()]:
                self.print_with_nl(f"{actor_name} has been already casted in {movie_title}!")
                continue
            role = self.get_str_from_user(f"Enter the role of {actor_name} in \"{movie_title}\".\n", duplicate=True)
            cast.append(actor_name)
            cast.append(string.capwords(role))
            if input("Do you want to add another role? Press y for yes.\n") not in ['y', 'Y']:
                break
        if cast:
            print(movie_title)
            for i in range(0, len(cast), 2):
                print(cast[i], 'as', cast[i + 1])
        validation = input(
            "Are you sure you want to add such data to cast database?\ny for yes\nn for no\nc for correct data\n")
        if validation == "y":
            self.add_to_txt_database('cast', [movie_title])
            for i in range(0, len(cast), 2):
                self.add_to_txt_database('cast', [f"{cast[i]} as {cast[i + 1]}"], without_new_line=True)
                self.my_movies.database[movie_title].add_cast(self.my_actors.database[cast[i]], cast[i + 1])
        elif validation == "c":
            self.add_cast_to_movie()
        else:
            self.intro()

    @staticmethod
    def print_with_nl(string):
        return print(string, end="\n")

    def look_for(self, search, database, text1, text2, text3="(Press 1 to quit this option)"):
        name = input(f"Please enter {search} you are looking for:\n").capitalize()
        temp = 0
        while name not in database:
            for data in database:
                if name.lower() == data.lower():
                    return data
                if re.search(name.lower(), data.lower()):
                    temp += 1
                    if temp == 1:
                        self.print_with_nl("Here are some suggestions:")
                    print(data)
            if name == '1':
                return
            line_printer.line()
            name = input(
                f"There is {text1} '{string.capwords(name)}' in my database."
                f"\nPlease enter {text2}\n{text3}\n")
        line_printer.line()
        return name

    def show_movie_info(self):
        movie_title = self.look_for("title of movie", self.my_movies.list_of_titles, "no movie titled",
                                    "correct or another title of movie.")
        print(self.my_movies.database[movie_title].introduce_myself())
        return self.my_movies.database[movie_title].show_cast()

    def show_actor_filmography(self):
        actor_name = self.look_for("name of actor/actress", self.my_actors.list_of_actors, "no such person",
                                   "correct or another name of actor/actress.")
        self.print_with_nl(self.my_actors.database[actor_name].introduce_myself())
        return self.my_actors.database[actor_name].show_filmography()

    def show_all_my_movies(self):
        self.print_with_nl("This is content of MyMovieDatabase:")
        return self.my_movies.print_database_content()

    def show_all_my_actors(self):
        self.print_with_nl("This is content of MyActorsDatabase:")
        return self.my_actors.print_database_content()

    def show_all_my_movies_with_cast(self):
        self.print_with_nl("This is my database of movies with cast:")
        time.sleep(1)
        print("(This will take a moment...)")
        time.sleep(2)
        for movie_title in self.my_movies.list_of_titles:
            this_movie = self.my_movies.database[movie_title]
            line_printer.line()
            time.sleep(0.5)
            print(movie_title, f'({this_movie.get_year_of_production()})')
            this_movie.show_cast()

    @staticmethod
    def exit_app():
        print("You've missed your chance to check out this wonderful program. Go and love yourself :)")
        exit(0)

    def intro(self):
        user_wish = "?"
        while user_wish not in self.options.keys():
            user_wish = input("""
    What would you like to do?\n
            1 - Show me alphabetical list of all my movies
            2 - Show me list of all my actors
            3 - Show me list of all my movies with cast
            4 - Look for an actor
            5 - Look for a movie
            6 - Add movie to database
            7 - Add actor to database
            8 - Add cast to movie
            0 - Nothing
    """)
        line_printer.line()
        self.options[user_wish]()
        line_printer.line()
        time.sleep(1)
        self.intro()


if __name__ == "__main__":
    MovieApplication()



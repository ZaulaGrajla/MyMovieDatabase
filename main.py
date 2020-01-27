import string
import time
from builtins import staticmethod

from actors import Actor
from database import MovieDatabase
from database.actors_database import ActorsDatabase
from movies import Movie
from readfromfiles.read_data_from_file import ReadCastFromTxt, ReadFromTxt
from tools import line_printer, add_to_txt_database, print_with_nl, check_if_in_db, get_str_from_user, \
    get_year_from_user, get_spec_str_from_user, look_for


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
        time.sleep(2)
        self.intro()

    def show_all_my_movies(self):
        print_with_nl("This is content of MyMovieDatabase:")
        return self.my_movies.print_database_content()

    def show_all_my_actors(self):
        print_with_nl("This is content of MyActorsDatabase:")
        return self.my_actors.print_database_content()

    def show_all_my_movies_with_cast(self):
        print_with_nl("This is my database of movies with cast:")
        time.sleep(1)
        print("(This will take a moment...)")
        time.sleep(2)
        for movie_title in self.my_movies.list_of_titles:
            this_movie = self.my_movies.database[movie_title]
            line_printer.line()
            time.sleep(0.5)
            print(movie_title, f'({this_movie.get_year_of_production()})')
            this_movie.show_cast()

    def show_actor_filmography(self):
        actor_name = look_for("name of actor/actress", self.my_actors.list_of_actors, "no such person",
                              "correct or another name of actor/actress.")
        print_with_nl(self.my_actors.database[actor_name].introduce_myself())
        return self.my_actors.database[actor_name].show_filmography()

    def show_movie_info(self):
        movie_title = look_for("title of movie", self.my_movies.list_of_titles, "no movie titled",
                               "correct or another title of movie.")
        print(self.my_movies.database[movie_title].introduce_myself())
        return self.my_movies.database[movie_title].show_cast()

    def add_movie_to_database(self):
        title = get_str_from_user("Please enter title of the movie.\n", "movie", "title of movie",
                                  self.my_movies.list_of_titles)
        genre = get_spec_str_from_user(Movie.MOVIE_TYPES, "a type of movie")
        year = get_year_from_user("year of production", 1899)
        line_printer.line()
        print("Title:", title, "\nType:", genre, "\nYear of production:", year)
        line_printer.line()
        self.add_data_valid('movies', [title, genre, year], self.my_movies, Movie)
        self.add_movie_to_database()

    def add_actor_to_database(self):
        sex = get_spec_str_from_user(['m', 'w'],
                                     "if this is an actor or an actress?\nPress 1 for man, 2 for woman",
                                     print_option=False)
        name = get_str_from_user(question="Please enter first name:\n", duplicate=True).capitalize()
        last_name = get_str_from_user(question="Please enter last name:\n", duplicate=True).capitalize()
        if check_if_in_db(name + ' ' + last_name, self.my_actors.list_of_actors):
            print("This person already exists in database! Please enter actor's data once again.\n")
            self.add_actor_to_database()
        country = get_str_from_user(question="Please enter country in which this person was born:\n",
                                    duplicate=True)
        b_year = get_year_from_user("year of birth", 1850)
        d_year = None
        if input("Is this person dead? Press y for yes, press any other key for no.\n") == 'y':
            d_year = get_year_from_user("year of death", b_year)
        line_printer.line()
        print("Name:", name, last_name, "\nCountry:", country, "\nYear of birth:", b_year)
        if d_year:
            print("Year of death:", d_year)
        line_printer.line()
        self.add_data_valid('actors', [name, last_name, b_year, country, sex, d_year], self.my_actors, Actor)
        self.add_actor_to_database()

    def add_cast_to_movie(self):
        print_with_nl("Warning! Actors and movies that you enter here as cast must already exist in database.\n")
        movie_title = look_for("title of movie", self.my_movies.list_of_titles, "no movie titled",
                               "correct title of movie.",
                               "Press 1 to return to menu and add new movie to database.")
        cast = []
        while movie_title:
            actor_name = look_for("name of actor/actress", self.my_actors.list_of_actors, "no such person",
                                  "correct name of actor/actress.",
                                  "Press 1 to return to menu and add new actor/actress to database.")
            if actor_name in [actor.get_name() for actor in self.my_movies.database[movie_title].cast.cast.keys()]:
                print_with_nl(f"{actor_name} has been already casted in {movie_title}!")
                continue
            role = get_str_from_user(f"Enter the role of {actor_name} in \"{movie_title}\".\n", duplicate=True)
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
            add_to_txt_database('cast', [movie_title])
            for i in range(0, len(cast), 2):
                add_to_txt_database('cast', [f"{cast[i]} as {cast[i + 1]}"], without_new_line=True)
                self.my_movies.database[movie_title].add_cast(self.my_actors.database[cast[i]], cast[i + 1])
        elif validation == "c":
            self.add_cast_to_movie()
        else:
            self.intro()

    def add_data_valid(self, db_txt: str, data: list, db_name, class_type):
        validation = input(
            "Are you sure you want to add this person to database?\ny for yes\nn for no\nc for correct data\n")
        if validation == "y":
            add_to_txt_database(db_txt, data)
            db_name.add_to_database(class_type(*data))
        elif validation == "c":
            return
        self.intro()

    @staticmethod
    def exit_app():
        print("You've missed your chance to check out this wonderful program. Go and love yourself :)")
        exit(0)


if __name__ == "__main__":
    MovieApplication()

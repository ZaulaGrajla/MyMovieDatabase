import datetime
import re
import time
from builtins import staticmethod
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

    @staticmethod
    def add_actor_to_database():
        print("This feature will be implemented soon")
        pass

    def add_movie_to_database(self):
        title = input("Please enter title of the movie.\n").capitalize()
        while title in self.my_movies.list_of_titles:
            title = input("This movie exists already in database!\nEnter another title of movie.\n").capitalize()
        for ind, typ in enumerate(Movie.MOVIE_TYPES):
            print(ind + 1, typ)
        genre = 0
        while genre not in range(1, len(Movie.MOVIE_TYPES) + 1):
            try:
                genre = int(input("Please choose a type of movie.\n"))
            except ValueError:
                continue
        genre = Movie.MOVIE_TYPES[genre - 1]
        year = 0
        while 1900 >= year or year >= int(datetime.datetime.strftime(datetime.datetime.now(), "%Y")):
            try:
                year = int(input("Please enter year of production.\n"))
            except ValueError:
                continue
        line_printer.line()
        print("Title:", title, "\nType:", genre, "\nYear of production:", year)
        line_printer.line()
        validation = input(
            "Are you sure you want to add such movie to database?\ny for yes\nn for no\nc for correct data\n")
        if validation == "y":
            with open('readfromfiles\\movies.txt', 'a+') as f:
                f.read()
                f.write(f'\n{title}, {genre}, {year},')
                self.my_movies.add_to_database(Movie(title, genre, year))
        elif validation == "c":
            self.add_movie_to_database()
        else:
            self.intro()

    @staticmethod
    def add_cast_to_movie():
        print("This feature will be implemented soon")
        pass

    @staticmethod
    def print_with_nl(string):
        return print(string, end="\n")

    def look_for(self, search, database, text1, text2):
        name = input(f"Please enter {search} you are looking for:\n").lower()
        temp = 0
        while name not in database:
            for data in database:
                if re.search(name.lower(), data.lower()):
                    temp += 1
                    if temp == 1:
                        self.print_with_nl("Here are some suggestions:")
                    print(data)
            if name == '1':
                return
            line_printer.line()
            name = input(
                f"There is {text1} '{name}' in my database."
                f"\nPlease enter {text2}\n(Press 1 to quit this option)\n")
        line_printer.line()
        return name

    def show_movie_info(self):
        movie_title = self.look_for("title of movie", self.my_movies.list_of_titles, "no movie titled",
                                    "correct or another title of movie.")
        if not movie_title:
            return
        print(self.my_movies.database[movie_title].introduce_myself())
        return self.my_movies.database[movie_title].show_cast()

    def show_actor_filmography(self):
        actor_name = self.look_for("name of actor/actress", self.my_actors.list_of_actors, "no such person",
                                   "correct or another name of actor/actress.")
        if not actor_name:
            return
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
        time.sleep(2)
        print("(This may take a moment...)")
        time.sleep(2)
        for movie_title in self.my_movies.list_of_titles:
            this_movie = self.my_movies.database[movie_title]
            line_printer.line()
            time.sleep(0.5)
            print(movie_title, f'({this_movie.get_year_of_production()})')
            this_movie.show_cast()
        pass

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
        time.sleep(2)
        self.intro()


if __name__ == "__main__":
    MovieApplication()

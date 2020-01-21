import time
from builtins import staticmethod
from functools import partial

from tools import line_printer

from database import MovieDatabase
from database.actors_database import ActorsDatabase
from readfromfiles.read_data_from_file import ReadCastFromTxt


class Options:
    pass


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

    @staticmethod
    def add_movie_to_database():
        print("This feature will be implemented soon")
        pass

    @staticmethod
    def add_cast_to_movie():
        print("This feature will be implemented soon")
        pass

    @staticmethod
    def print_with_nl():
        return partial(print, end="\n")

    def show_movie_info(self):
        movie_title = input("Please enter title of movie you are looking for:\n")
        while movie_title not in self.my_movies.database.keys():
            movie_title = input(
                "There is no such movie in my database."
                "\nPlease enter another title of movie.\n(Press 1 to quit)\n")
            if movie_title == '1':
                self.exit_app()
        line_printer.line()
        print(self.my_movies.database[movie_title].introduce_myself())
        return self.my_movies.database[movie_title].show_cast()

    def show_actor_filmography(self):
        actor_name = input("Please enter name of actor/actress you are looking for:\n")
        while actor_name not in self.my_actors.database.keys():
            actor_name = input(
                "There is no such person in my database."
                "\nPlease enter another name of actor/actress.\n(Press 1 to quit)\n")
            if actor_name == '1':
                self.exit_app()
        line_printer.line()
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
            this_movie=self.my_movies.database[movie_title]
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
            user_wish = input("\nWhat would you like to do?\n"
                              "1 - Show list of all my movies\n"
                              "2 - Show list of all my actors\n"
                              "3 - Show list of all my movies with cast\n"
                              "4 - Look for actor\n"
                              "5 - Look for movie\n"
                              "6 - Add movie to database\n"
                              "7 - Add actor to database\n"
                              "8 - Add cast to movie\n"
                              "0 - Nothing\n")
        line_printer.line()
        self.options[user_wish]()
        line_printer.line()
        time.sleep(5)
        self.intro()


if __name__ == "__main__":
    MovieApplication()



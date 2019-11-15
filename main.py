import time

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
            '3': self.show_all_my_movies_with_cast,
            '2': self.show_all_my_actors,
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

    def show_movie_info(self):
        movie_title = input("Please enter title of movie you are looking for:\n")
        while movie_title not in self.my_movies.database.keys():
            movie_title = input(
                "There is no such movie in my database."
                "\nPlease enter another title of movie.\n(Press 1 to quit)\n")
            if movie_title == '1':
                self.exit_app()
        print('\n___________________________________________________________________')
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
        print('\n___________________________________________________________________')
        print(self.my_actors.database[actor_name].introduce_myself(), '\n')
        return self.my_actors.database[actor_name].show_filmography()

    def show_all_my_movies(self):
        print("This is content of MyMovieDatabase:\n")
        return self.my_movies.print_database_content()

    def show_all_my_actors(self):
        print("This is content of MyActorsDatabase:\n")
        return self.my_actors.print_database_content()

    def show_all_my_movies_with_cast(self):
        print("This is my database of movies with cast:\n")
        time.sleep(2)
        print("(This will take a moment...)")
        time.sleep(2)
        for movie_title in self.my_movies.list_of_titles:
            this_movie=self.my_movies.database[movie_title]
            print('___________________________________________________________________')
            time.sleep(0.3)
            print(movie_title, f'({this_movie.get_year_of_production()})')
            this_movie.show_cast()

        return

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
        print('\n___________________________________________________________________')
        self.options[user_wish]()
        print('___________________________________________________________________')
        time.sleep(5)
        self.intro()


if __name__ == "__main__":
    MovieApplication()

# Tak naprawdę trzeba zaimplementować jeszcze tylko dodawanie nowych filmów i aktorów
# zaznacz resztę że not implemented
# i może tak żeby można było wpisywać nazwę obojętnie jakimi literami a i tak znajdzie film
# po gatunku żeby można było szukać
# dodać ocenę do filmu

# Klasa film i klasa aktor
# Plik tekstowy z imionami nazwiskami rokiem urodzenia i krajem pochodzenia aktorów
# Plik tekstowy z filmami tytuł rok gatunek
# W filmach do dodania jest opis i ocena
# W mainie można zrobić tak:
# wyświetlić bazę filmów (alfabetycznie, rocznikami lub gatunkami)
# wtedy zaczytuje cały plik tekstowy
# wyświetlić bazę aktorów - alfabetycznie
# szukać filmu lub aktora - trzeba podać poprawnie imię lub nazwisko lub tytuł
# wtedy zaczyta tylko tę linijkę z pliku tekstowego
# w filmie można dodać opis lub ocenę lub obsade
# U aktorów wyświetlić filmy z bazy do których są podpięci
# Baza filmów: "Tytuł filmu": obiekt film
# Baza aktor: "Imię i nazwisko": obiekt aktor

# Movie:
# tytuł, rok, gatunek w inicie
# do dodania opis, ocena
# self.cast=Cast()
# w klasie Cast mamy defa który dodaje aktora i rolę którą grał w inicie może być proszony reżyser isinstance
# jeden def co returnuje dict{} z cast najlepiej może nawet printuje listę actor as role
# do dodania obsada: {obiekt aktor:rola którą grał + tu reżyser na pierwszym miejscu}
# za każdym razem jak dodajemy aktora do obsady to w jego filmografii pojawia się tytuł filmu rocznik i rola
# możemy analogicznie zrobić funkcję z usuwaniem

# Actor:
# imię, nazwisko, rok urodzenia, kraj pochodzenia
# filmografia: obiekty (nie dodajemy filmów do filmografii - założenie jest, że dodajemy filmy do bazy)
# filmografia to też może być mała klasa która będzie przechowywała tytuł filmu rocznik i rolę

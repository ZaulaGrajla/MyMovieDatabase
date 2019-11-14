import time

from database import MovieDatabase
from database.actors_database import ActorsDatabase
from readfromfiles.read_data_from_file import ReadActorsFromTxt, ReadMoviesFromTxt, ReadCastFromTxt


class MovieApplication:

    def __init__(self):
        self.my_movies = MovieDatabase()
        self.my_actors = ActorsDatabase()
        ReadCastFromTxt().read_cast(self.my_movies, self.my_actors)
        self.intro()

    def show_all_my_movies(self):
        return self.my_movies.print_database_content()


    def show_all_my_actors(self):
        return self.my_actors.print_database_content()


    def show_all_my_movies_with_cast(self):
        print("This is my database of movies with cast:\n")
        for movie_title in self.my_movies.list_of_titles:
            # time.sleep(1)
            print(movie_title)
            self.my_movies.database[movie_title].show_cast()
        return

    def intro(self):
        user = input("\nWhat would you like to see?\n1 - List of my movies\n2 - List of my actors\n"
                     "3 - List of my movies with cast\n0 - Nothing\n")
        while user not in ['1', '2', '3', '0']:
            user = input("What would you like to see?\n1 - List of my movies\n2 - List of my actors\n"
                         "3 - List of my movies with cast\n0 - Nothing\n")
        if user == '1':
            self.show_all_my_movies()
            self.intro()
        elif user == '2':
            self.show_all_my_actors()
            self.intro()
        elif user == '3':
            self.show_all_my_movies_with_cast()
            self.intro()
        elif user == '0':
            print("You've missed your chance to check out this wonderful program. Go and love yourself :)")
            exit(0)


if __name__ == "__main__":
    MovieApplication()

# zrobił się syf
# DONE syf z tym czy jest kropka w read files czy nie w importowanych modułach
# to wszystko trzeba by porozdzielać i zrobić bardziej przejrzyste drzewko
# zmień to z Read coś tam na My MovieDatabase w inicie będzie Readowanie czyli zaczytywanie read_from_file() i def read
# MyActors Database to samo będzie zaczytywanie ale już przechowalnia
# uwspólnij te databases
# Singletony? Chyba na razie nie.
# Cast potrzebuje aktorów i filmów więc jeśli nie będzie tych filmów w bazie to nie można dodać cast
# a jeżeli będzie film ale nie actor to utworzy się nowy actor w bazie
# main będzie wywoływał MyMovieDatabase()
# MyActorsDatabase()
# my_movies=MyMovieDatabase().database
# my_actors=MyActorsDatabase().database
# CastDatabase(my_movies,my_actors)


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


# # harrison=Actor("Harrison","Ford",1942,"USA")
# # indiana = Movie("Raiders of the lost ark", 1980)
# # # harrison.filmography.add_movie(indiana, "Indiana Jones")
# #
# harrison = Actor('Harrison', "Ford",1942, "USA")
# indiana = Movie("Raiders of the lost ark","adventure", 1980)
# indiana2 = Movie("Temple of doom", "adventure",1980)
# indiana3 = Movie("Indiana Jones and the last Crusade", "adventure",1989)
# starwarsy=Movie("Star Wars: Episode IV New Hope", "fantasy",1977)
# # indiana.add_cast(harrison, "Indiana Jones")
# # indiana.show_cast()
# # print(indiana)
# print(indiana.get_title())
# # harrison.filmography.add_movie(indiana,"Indiana Jones")
# # harrison.filmography.add_movie(indiana2,"Indiana Jones")
# # harrison.filmography.add_movie(indiana3,"Indiana Jones")
# # harrison.filmography.add_movie(starwarsy,"Han Solo")
# #
# harrison.filmography.print_filmography()
# print(harrison.filmography.active_years)
# indiana.add_cast(harrison,"Indiana Jones")
# willie=Actor("Cate","Spielberg",1960,"USA","Female")
# indiana.add_cast(willie,"Willie Scott")
# # harrison.filmography.print_filmography()
# indiana.show_cast()

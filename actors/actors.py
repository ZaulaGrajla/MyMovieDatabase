import datetime
from converters.age_converter import YearIntoAgeConverter
from abc import abstractmethod


class Filmography:

    def __init__(self):
        self.filmography = []
        self.active_years = set()

    def add_movie(self, movie, role: str):
        self.filmography.append({movie.get_year_of_production(): [movie.get_title(), role]})
        self.active_years.add(movie.get_year_of_production())

    def print_filmography(self):
        for year in self.active_years:
            for position in self.filmography:
                if year in position.keys():
                    print('%4s \t %24s \t as %16s' % (year, position[year][0], position[year][1]))


class Human():

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_age(self):
        pass

    @abstractmethod
    def get_country(self):
        pass

    @abstractmethod
    def introduce_myself(self):
        pass

    @abstractmethod
    def get_sex(self):
        pass


class Director(Human):
    def __init__(self, first_name: str, last_name: str, birth_year=None, country=None, sex='Male'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.name = f'{self.first_name} {self.last_name}'
        self.country = country
        self.filmography = Filmography()
        self.sex = sex

    def get_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        return YearIntoAgeConverter(self.birth_year).get_age()

    def get_country(self):
        return self.country

    def introduce_myself(self):
        return f"Director {self.get_name()} is {self.get_age()} years old"


class Actor(Human):
    def __init__(self, first_name: str, last_name: str, birth_year: int, country=None, sex='Male'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.country = country
        self.filmography = Filmography()
        self.sex = sex

    def get_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        return YearIntoAgeConverter(self.birth_year).get_age()

    def get_country(self):
        return self.country

    def introduce_myself(self):
        sex = "Actor"
        origin = "."
        if self.sex != "Male":
            sex = "Actress"
        if self.country:
            origin = f" and comes from {self.country}."
        return f"{sex} {self.get_name()} is {self.get_age()} years old{origin}"

hAR=Actor("Harrison","Ford",1942,"USA")
print(hAR.introduce_myself())
print(hAR.get_name())
print(hAR.get_age())

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

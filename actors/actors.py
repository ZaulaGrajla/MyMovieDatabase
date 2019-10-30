import datetime
from converters.age_converter import YearIntoAgeConverter


class Human():

    def get_name(self):
        pass

    def get_age(self):
        pass

    def get_country(self):
        pass

    def add_movie_to_filmography(self, movie):
        pass

    def introduce_myself(self):
        pass

    def get_sex(self):
        pass

class Actor(Human):
    def __init__(self, first_name: str, last_name: str, birth_year: int, country=None, sex='Male'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.name=f'{self.first_name} {self.last_name}'
        self.country=country
        self.filmography=[]
        self.sex='Male'


    def get_name(self):
        return self.name


    def get_age(self):
        return YearIntoAgeConverter(self.birth_year)


    def get_country(self):
        return self.country


    def add_movie_to_filmography(self, movie):
        self.filmography.append(movie)

    def introduce_myself(self):
        if self.sex=="Male":
            return f"Actor {self.name} is {self.get_age()} years old"
        else:
            return f"Actress {self.name} is {self.get_age()} years old"


actor=Actor('Harrison','Ford',1942,'USA')


# aktor będzie miał wiek, imię i kraj pochodzenia
# przy jego przedstawieniu potrzebna jest lista filmów do wyświetlenia
# te filmy są obiektami, więc wyświetlając aktora chcę przejść od filmu
# baza filmowa będzie miała filmy, każdy z nich ma tytuł, reżysera, opis, rocznik, aktórów i moją skalę miłości,
# gatunek
#  + countdown ile razy obejrzałam ale to potem
# w mainie można wyświetlić listę alfabetycznie
# lub wg mojej oceny
# lub wg gatunku

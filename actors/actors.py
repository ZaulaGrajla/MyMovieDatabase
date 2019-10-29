import datetime


class Human():

    def __init__(self, name: str, birth_date: str):
        self.name = name
        self.birth_date = birth_date

    def get_name(self):
        pass

    def get_age(self):
        pass

    def get_country(self):
        pass

    def add_movie_to_filmography(self, movie):
        pass


class Actor:
    pass


now = datetime.date.today()
print(now)

# aktor będzie miał wiek, imię i kraj pochodzenia
# przy jego przedstawieniu potrzebna jest lista filmów do wyświetlenia
# te filmy są obiektami, więc wyświetlając aktora chcę przejść od filmu
# baza filmowa będzie miała filmy, każdy z nich ma tytuł, reżysera, opis, rocznik, aktórów i moją skalę miłości,
# gatunek
#  + countdown ile razy obejrzałam ale to potem
# w mainie można wyświetlić listę alfabetycznie
# lub wg mojej oceny
# lub wg gatunku
import datetime
from tools.age_converter import YearIntoAgeConverter
from abc import abstractmethod


class Filmography:

    def __init__(self):
        self.filmography = []
        self.active_years = set()

    def add_movie(self, movie, role: str):
        self.filmography.append({int(movie.get_year_of_production()): [movie.get_title(), role]})
        self.active_years.add(int(movie.get_year_of_production()))

    def print_filmography(self):
        self.active_years = sorted((list(self.active_years)))
        for year in self.active_years:
            for position in self.filmography:
                if year in position.keys():
                    print('%4s \t %48s \t as %16s' % (year, position[year][0], position[year][1]))
        self.active_years = set(self.active_years)


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
    def __init__(self, first_name: str, last_name: str, birth_year=None, country=None, sex='m'):
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
    def __init__(self, first_name: str, last_name: str, birth_year: int = None, country=None, sex='m',
                 death_year=None, ):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = int(birth_year)
        self.country = country
        self.filmography = Filmography()
        self.sex = sex
        if death_year is not None:
            self.death_year = int(death_year)
        else:
            self.death_year = death_year

    def get_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        if self.birth_year is None:
            return "No data for birthday"
        return YearIntoAgeConverter(self.birth_year, self.death_year).get_age()

    def get_country(self):
        return self.country

    def introduce_myself(self):
        sex = "Actor"
        origin = "."
        if self.sex != "m":
            sex = "Actress"
        if self.country:
            origin = f" and comes from {self.country}"
        if self.death_year is not None:
            return f"{sex} {self.get_name()} was born in {self.birth_year} in {self.country} " \
                   f"and died in {self.death_year} at the age of {self.get_age()}."
        if self.birth_year is None:
            return f"{sex} {self.get_name()}"
        return f"{sex} {self.get_name()} is {self.get_age()} years old{origin}."

    def show_filmography(self):
        return self.filmography.print_filmography()

import datetime


class YearIntoAgeConverter:
    """converts integer with birth year from user into age"""

    def __init__(self, birth_year, death_year=None):
        self.birth_year = birth_year
        self.death_year = death_year
        self.validate()

    # def __repr__(self):
    #     return f'This converter will tell you how many years old is someone born in {self.birth_year}'

    def validate(self):
        dates = [self.birth_year]
        if self.death_year is not None:
            if self.death_year < self.birth_year:
                raise ValueError("Death cannot happen before birthday")
            dates.append(self.death_year)
        for date in dates:
            if type(date) != int or 1850 > date > int(datetime.datetime.strftime(datetime.datetime.now(), "%Y")):
                raise ValueError("Incorrect year format!")

    def get_age(self):
        if self.death_year is not None:
            return self.death_year - self.birth_year
        return int(datetime.datetime.strftime(datetime.datetime.now(), "%Y")) - self.birth_year

import datetime


class YearIntoAgeConverter:
    """converts integer with birth year from user into age"""

    current_year = int(datetime.datetime.strftime(datetime.datetime.now(), "%Y"))

    def __init__(self, birthyear):
        self.birthyear = birthyear
        self.validate()

    # def __repr__(self):
    #     return f'This converter will tell you how many years old is someone born in {self.birthyear}'

    def validate(self):
        if type(self.birthyear) != int \
                or self.birthyear < 1850 \
                or self.birthyear > self.current_year:
            raise ValueError("Incorrect year format!")

    def get_age(self):
        return self.current_year-self.birthyear




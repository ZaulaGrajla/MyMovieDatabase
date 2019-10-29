import datetime


class StringIntoAgeConverter:
    """converts string from user containing birthday in format YYYY-MM-DD into age"""

    def __init__(self, birthday):
        self.birthday = birthday
        self.validate()

    def validate(self):
        correct_birthday_string_length = 10
        months_with_30_days = [4, 6, 9, 11]
        months_with_28_days = [2]
        months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
        months_number = 12
        if len(self.birthday) != correct_birthday_string_length or " " in self.birthday:
            raise ValueError("Check length of input and white-space characters!")
        try:
            year, month, day = self.birthday.split("-")[0], self.birthday.split("-")[1], self.birthday.split("-")[2]
            year, month, day = int(year), int(month), int(day)
            current_year = int(datetime.datetime.strftime(datetime.datetime.now(), "%Y"))
            if year >= current_year:
                raise ValueError(
                    f"We have year {current_year}. This man has just been born. Please give a lesser number!")
            if month > months_number:
                raise ValueError("There are 12 months in the year!")
            if day > 31:
                raise ValueError("There is no such long month")
            elif day == 31 and not month in months_with_31_days:
                raise ValueError("This month is not 31 days long")
            elif day in [30, 29] and month in months_with_28_days:
                raise ValueError("This month is not 30")
            elif day == 29 and month == 2 and year % 4 != 0:
                raise ValueError("This year is not leap!")
        except IndexError:
            print("Check if '-' is in correct place!")
            raise IndexError
        except ValueError:
            print("Check if your date contains only integers!")
            raise ValueError

    def get_age(self):
        current_date = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")
        current_date=datetime.datetime.strptime(current_date,"%Y-%m-%d")
        birth_date = datetime.datetime.strptime(self.birthday, "%Y-%m-%d")

        print(type(current_date))
        print(type(birth_date))
        return current_date-birth_date



# StringIntoAgeConverter(1234).get_age()
print(datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d"))
a=StringIntoAgeConverter("1992-12-12").get_age()
print(a)

import datetime

from .if_in_db_checker import check_if_in_db


def get_str_from_user(question, text1='?', text2='?', database=[], duplicate=False):
    data = input(question).capitalize()
    while not duplicate and check_if_in_db(data, database):
        data = input(f"This {text1} exists already in database!\nEnter another {text2}.\n").capitalize()
    return data


def get_spec_str_from_user(list_to_choose, options: str, print_option=True):
    if print_option:
        for ind, typ in enumerate(list_to_choose):
            print(ind + 1, typ)
    option = 0
    while option not in range(1, len(list_to_choose) + 1):
        try:
            option = int(input(f"Please choose {options}.\n"))
        except ValueError:
            continue
    return list_to_choose[option - 1]


def get_year_from_user(text1, year_to_compare=None):
    year = 0
    while 1900 > year or year > int(datetime.datetime.strftime(datetime.datetime.now(), "%Y")):
        try:
            year = int(input(f"Please enter {text1}.\n"))
            if year_to_compare:
                if year < year_to_compare:
                    print(f"This year cannot be former than {year_to_compare}")
                    year = 0
        except ValueError:
            continue
    return year

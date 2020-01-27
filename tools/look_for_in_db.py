import re

from tools import print_with_nl
from tools import line
from string import capwords


def look_for(search, database, text1, text2, text3="(Press 1 to quit this option)"):
    name = input(f"Please enter {search} you are looking for:\n").capitalize()
    temp = 0
    while name not in database:
        for data in database:
            if name.lower() == data.lower():
                return data
            if re.search(name.lower(), data.lower()):
                temp += 1
                if temp == 1:
                    print_with_nl("Here are some suggestions:")
                print(data)
        if name == '1':
            return
        line()
        name = input(
            f"There is {text1} '{capwords(name)}' in my database."
            f"\nPlease enter {text2}\n{text3}\n")
    line()
    return name

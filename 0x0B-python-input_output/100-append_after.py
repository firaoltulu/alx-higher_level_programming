#!/usr/bin/python3
"""
This Contains the "append after" function.
"""

def append_after(filename="", search_string="", new_string=""):
    """This appends "new_string" after a line containing
    "search_string" in "filename". """
    with open(filename, 'r', encoding='utf-8') as f:
        one = []
        while True:
            two = f.readline()
            if two == "":
                break
            one.append(two)
            if search_string in two:
                one.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(one)

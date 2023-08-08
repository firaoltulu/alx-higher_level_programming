#!/usr/bin/python3

"""This Function Print a string in uppercase."""
"""@str: Is a string to be printed In uppercase."""
def uppercase(str):
    for six in str:
        if ord(six) >= 97 and ord(six) <= 122:
            six = chr(ord(six) - 32)
        print("{}".format(six), end="")
    print("")

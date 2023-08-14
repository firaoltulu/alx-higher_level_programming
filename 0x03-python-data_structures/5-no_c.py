#!/usr/bin/python3
# 5-no_c.py

"""This Function Remove all characters c and C from a string."""
def no_c(my_string):
    copy = [one for one in my_string if one != 'c' and one != 'C']
    return ("".join(copy))

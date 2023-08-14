#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    copy = [one for one in my_string if one != 'c' and one != 'C']
    return ("".join(copy))

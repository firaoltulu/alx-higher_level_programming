#!/usr/bin/python3
# 9-max_integer.py

"""This Function Find the biggest integer of a list."""
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    one = my_list[0]
    for two in range(len(my_list)):
        if my_list[two] > one:
            one = my_list[two]

    return (one)

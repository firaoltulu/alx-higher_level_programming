#!/usr/bin/python3
# 3-print_reversed_list_integer.py

"""This function Print all integers of a list in reverse order."""
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        my_list.reverse()
        for one in my_list:
            print("{:d}".format(one))

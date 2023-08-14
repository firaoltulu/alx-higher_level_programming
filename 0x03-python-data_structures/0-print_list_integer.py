#!/usr/bin/python3
# 0-print_list_integer.py

"""This Program Print all integers of a list."""
def print_list_integer(my_list=[]):
    for one in range(len(my_list)):
        print("{:d}".format(my_list[one]))

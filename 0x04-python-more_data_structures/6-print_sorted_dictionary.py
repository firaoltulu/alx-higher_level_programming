#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    two = list(a_dictionary.keys())
    two.sort()
    for one in two:
        print("{}: {}".format(one, a_dictionary.get(one)))

#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    two = a_dictionary.copy()
    one = list(two.keys())

    for i in one:
        two[i] *= 2

    return (two)

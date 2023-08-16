#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    three = list(a_dictionary.keys())

    for one in three:
        if value == a_dictionary.get(one):
            del a_dictionary[one]

    return (a_dictionary)

#!/usr/bin/python3

"""This program Print all possible different combinations of two digits in ascending order."""
for five in range(0, 10):
    for six in range(five + 1, 10):
        if five == 8 and six == 9:
            print("{}{}".format(five, six))
        else:
            print("{}{}".format(five, six), end=", ")

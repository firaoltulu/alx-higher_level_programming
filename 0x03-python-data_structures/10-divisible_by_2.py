#!/usr/bin/python3
# 10-divisible_by_2.py

"""This Function Find all multiples of 2 in a list."""
def divisible_by_2(my_list=[]):
    one = []
    for two in range(len(my_list)):
        if my_list[two] % 2 == 0:
            one.append(True)
        else:
            one.append(False)

    return (one)

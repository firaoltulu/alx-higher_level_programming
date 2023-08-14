#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for one in matrix:
        for two in one:
            print("{:d}".format(two), end=" " if two != one[-1] else "")
        print()

#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda one: list(map(lambda two: two**2, one)), matrix)))

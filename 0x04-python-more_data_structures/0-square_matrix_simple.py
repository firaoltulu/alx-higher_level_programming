#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for one in range(len(matrix)):
        new_matrix[one] = list(map(lambda two: two**2, matrix[one]))

    return (new_matrix)

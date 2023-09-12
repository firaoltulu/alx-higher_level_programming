#!/usr/bin/python3
"""This Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """This Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    one = [[1]]
    while len(one) != n:
        two = one[-1]
        three = [1]
        for i in range(len(two) - 1):
            three.append(two[i] + two[i + 1])
        three.append(1)
        one.append(three)
    return one

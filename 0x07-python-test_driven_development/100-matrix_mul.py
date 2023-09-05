#!/usr/bin/python3
"""This module contain a function that multiplies two matrix"""


def matrix_mul(m_a, m_b):
    """This is a matrix_mul function that multiplies two matrix.
    Args:
        m_a: is the first matrix.
        m_b: Is the second matrix.
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")


    four = 0
    one = 0


    if m_a == []:
        raise ValueError("m_a can't be empty")
    for two in m_a:
        if type(two) != list:
            raise TypeError("m_a must be a list of lists")
        three = len(m_a[0])
        if two == []:
            raise ValueError("m_a can't be empty")
        if three != len(two):
            raise TypeError("each row of m_a must be of the same size")
        four = len(two)
        for five in two:
            if type(five) != int and type(five) != float:
                raise TypeError("m_a should contain only integers or floats")


    if m_b == []:
        raise ValueError("m_b can't be empty")
    for six in m_b:
        if type(six) != list:
            raise TypeError("m_b must be a list of lists")
        seven = len(m_b[0])
        if six == []:
            raise ValueError("m_b can't be empty")
        if seven != len(six):
            raise TypeError("each row of m_b must be of the same size")
        one += 1
        for eight in six:
            if type(eight) != int and type(eight) != float:
                raise TypeError("m_b should contain only integers or floats")


    if four != one:
        raise ValueError("m_a and m_b can't be multiplied")

    mul_matrix = []

    for nine in m_a:
        l = 0
        ten = []
        while l < len(m_b[0]):
            result = 0
            k = 0
            for column_1 in nine:
                result += column_1 * m_b[k][l]
                k += 1
            ten.append(result)
            l += 1
        mul_matrix.append(ten)

    return mul_matrix

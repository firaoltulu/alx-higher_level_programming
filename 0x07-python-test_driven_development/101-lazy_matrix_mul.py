#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""This Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """This Return the multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): Is The first matrix.
        m_b (list of lists of ints/floats): Is The second matrix.
    """

    return (np.matmul(m_a, m_b))

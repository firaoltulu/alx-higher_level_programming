#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """This Class Represent a square.

     Attributes:
        __size (int): size of the new square.
    """

    def __init__(self, size=0):
        """this function Initialize a new Square.

        Args:
            size (int): int that contains
                        The size of the new square
                        Default to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

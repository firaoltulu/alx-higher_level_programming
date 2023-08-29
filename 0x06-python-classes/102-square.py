#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """This class Represent a square.

    Attributes:
        size (int): size of the new square.
    """

    def __init__(self, size=0):
        """this method Initialize a new square.

        Args:
            size (int): Int that contains
                        The size of the new square
                        Default to 0.
        """
        self.size = size

    @property
    def size(self):
        """This Method Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return: the current area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()


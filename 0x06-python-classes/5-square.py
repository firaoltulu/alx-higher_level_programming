#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """This class Represent a square.

    Attributes:
        size (int): size of the new square.
    """

    def __init__(self, size):
        """This method Initialize a new square.

        Args:
            size (int): Int that contains
                        The size of the new square
                        Default to 0.
        """
        self.size = size

    @property
    def size(self):
        """This method Get/set the current size of the square."""
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

    def my_print(self):
        """This Method Print the square with the # character."""
        for one in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

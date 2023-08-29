#!/usr/bin/python3

class Square:
    """This Class Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """This Method Initialize a new square.

        Arguments:
            size (int): Int that contains
                        The size of the new square
                        Default to 0.
            position (int, int): Array Int that contains
                        The position of the new square
                        Default to 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """This Method Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return: the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """This Method Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for one in range(0, self.__position[1])]
        for two in range(0, self.__size):
            [print(" ", end="") for three in range(0, self.__position[0])]
            [print("#", end="") for four in range(0, self.__size)]
            print("")

    def __str__(self):
        """This Method Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for one in range(0, self.__position[1])]
        for two in range(0, self.__size):
            [print(" ", end="") for three in range(0, self.__position[0])]
            [print("#", end="") for four in range(0, self.__size)]
            if two != self.__size - 1:
                print("")
        return ("")


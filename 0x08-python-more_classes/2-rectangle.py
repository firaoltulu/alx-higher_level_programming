#!/usr/bin/python3
"""
This Defines a class Rectangle.
"""

class Rectangle:
    """This is a Representation of a rectangle."""
    def __init__(self, width=0, height=0):
        """This Initializes the rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """This is Getter for the private instance attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """This is Setter for the private instance attribute width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This is Getter for the private instance attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private instance attribute height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

#!/usr/bin/python3
"""
This Defines a class Rectangle.
"""


class Rectangle:
    """This is a Representation of a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """This Initializes the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """This prints a string when an instance has been deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """This getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """This returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """This returns printable string representation of the rectangle"""
        one = ""
        if self.__width != 0 and self.__height != 0:
            one += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return one

    def __repr__(self):
        """This returns a string representation of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

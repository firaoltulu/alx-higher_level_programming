#!/usr/bin/python3
"""
This module contains the "Square" class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """This Initialize a new Square.
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """This Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """This Update the Square.
        Args:
            *args (ints): New attribute values.
                - first argument represents id attribute
                - second argument represents size attribute
                - third argument represents x attribute
                - fourth argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            one = 0
            for arg in args:
                if one == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif one == 1:
                    self.size = arg
                elif one == 2:
                    self.x = arg
                elif one == 3:
                    self.y = arg
                one += 1

        elif kwargs and len(kwargs) != 0:
            for one, two in kwargs.items():
                if one == "id":
                    if two is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = two
                elif one == "size":
                    self.size = two
                elif one == "x":
                    self.x = two
                elif one == "y":
                    self.y = two

    def to_dictionary(self):
        """This Return the dictionary representation of the Square."""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }

        def __str__(self):
            """This Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.width)

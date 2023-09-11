#!/usr/bin/python3
"""
This Contains the class MyInt
"""


class MyInt(int):
    """THis is a rebel version of an integer, perfect for opposite day!"""
    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """THis function does what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """THis function does what was == is now !="""
        return int(self) == other

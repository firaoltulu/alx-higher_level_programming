#!/usr/bin/python3
"""
This Contains the clas "Student".
"""


class Student:
    """This Representation of a student."""
    def __init__(self, first_name, last_name, age):
        """This Initializes the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This returns a dictionary representation of a Student instance"""
        return self.__dict__

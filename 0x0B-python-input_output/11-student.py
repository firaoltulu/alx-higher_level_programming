#!/usr/bin/python3
"""
This Contains the clas "Student".
"""


class Student:
    """THis Representation of a student."""
    def __init__(self, first_name, last_name, age):
        """THis Initializes the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """THis returns a dictionary representation of a Student instance
        with specified attributes."""
        if attrs is None:
            return self.__dict__
        one = {}
        for two in attrs:
            try:
                one[two] = self.__dict__[two]
            except FileNotFoundError:
                pass
        return one

    def reload_from_json(self, json):
        """THis replaces all attributes of the Student instance"""
        for one in json:
            try:
                setattr(self, one, json[one])
            except FileNotFoundError:
                pass

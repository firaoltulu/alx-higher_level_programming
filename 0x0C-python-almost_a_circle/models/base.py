#!/usr/bin/python3
"""This Defines a base model class."""
import json
import csv
import turtle


class Base:
    """This Represent the base model.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """This Initialize a new Base.
        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This Return the JSON serialization of a list of dicts.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This Write the JSON serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        one = cls.__name__ + ".json"
        with open(one, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                two = [three.to_dictionary() for three in list_objs]
                jsonfile.write(Base.to_json_string(two))

    @staticmethod
    def from_json_string(json_string):
        """This Return the deserialization of a JSON string.
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """This Return a class instantied from a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                one = cls(1, 1)
            else:
                one = cls(1)
            one.update(**dictionary)
            return one

    @classmethod
    def load_from_file(cls):
        """This Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        two = str(cls.__name__) + ".json"
        try:
            with open(two, "r") as jsonfile:
                three = Base.from_json_string(jsonfile.read())
                return [cls.create(**one) for one in three]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """This Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        one = cls.__name__ + ".csv"
        with open(one, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    two = ["id", "width", "height", "x", "y"]
                else:
                    two = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=two)
                for three in list_objs:
                    writer.writerow(three.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """This Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        one = cls.__name__ + ".csv"
        try:
            with open(one, "r", newline="") as two:
                if cls.__name__ == "Rectangle":
                    three = ["id", "width", "height", "x", "y"]
                else:
                    three = ["id", "size", "x", "y"]
                four = csv.DictReader(two, fieldnames=three)
                four = [dict([five, int(six)] for five, six in seven.items())
                        for seven in four]
                return [cls.create(**seven) for seven in four]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """This Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        one = turtle.Turtle()
        one.screen.bgcolor("#b7312c")
        one.pensize(3)
        one.shape("turtle")

        one.color("#ffffff")
        for four in list_rectangles:
            one.showturtle()
            one.up()
            one.goto(four.x, four.y)
            one.down()
            for i in range(2):
                one.forward(four.width)
                one.left(90)
                one.forward(four.height)
                one.left(90)
            one.hideturtle()

        one.color("#b5e3d8")
        for two in list_squares:
            one.showturtle()
            one.up()
            one.goto(two.x, two.y)
            one.down()
            for three in range(2):
                one.forward(two.width)
                one.left(90)
                one.forward(two.height)
                one.left(90)
            one.hideturtle()

        turtle.exitonclick()


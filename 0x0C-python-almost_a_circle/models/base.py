#!/usr/bin/python3
"""Contains a base class for the model"""
import json
import csv
import turtle


class Base:
    """A class that serves as the base for other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): a list of dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): a list of instances who inherits from Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation

        Args:
            json_string (str): the string representing a list of dictionaries
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set

        Args:
            dictionary (dict): dictionary containing the attributes
        """
        polygons = {
            'Rectangle': (1, 1, 0, 0),
            'Square': (1, 0, 0, None)
        }
        if cls.__name__ in polygons.keys():
            polygon = cls(*polygons[cls.__name__])
            polygon.update(**dictionary)
            return polygon

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, encoding="utf-8") as f:
                list_instances = cls.from_json_string(f.read())
                return [cls.create(**d) for d in list_instances]
        except IOError:
            return []

    @staticmethod
    def _build_fieldnames(c):
        """build the fieldnames for the csv reader or writer based on class"""
        if c.__name__ == "Rectangle":
            return ["id", "width", "height", "x", "y"]
        else:
            return ["id", "size", "x", "y"]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes a list of python obj into a csv format
        and saves it to a file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                writer = csv.DictWriter(f,
                                        fieldnames=cls._build_fieldnames(cls))
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a CSV string representation to a python object"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, encoding="utf-8") as f:
                reader = csv.DictReader(f,
                                        fieldnames=cls._build_fieldnames(cls))
                list_dicts = [dict((k, int(v)) for k, v in d.items())
                              for d in reader]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares

        Args:
            list_rectangles (list): a list of rectangle objects to draw.
            list_squares (list): a list of square objects to draw
        """
        t = turtle.Turtle()
        t.screen.bgcolor("brown")
        t.hideturtle()

        def show(color, objects):
            """Show the object on the screen"""
            t.color(color)
            for obj in objects:
                t.penup()
                t.goto(obj.x, obj.y)
                t.pendown()

                for i in range(2):
                    t.forward(obj.width)
                    t.left(90)
                    t.forward(obj.height)
                    t.left(90)

        show("gold", list_rectangles)
        show("magenta", list_squares)

        turtle.exitonclick()

#!/usr/bin/python3
"""A module that contains a Rectangle class"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize the Rectangle class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """computes the area of itself"""
        return self.__width * self.__height

    def __str__(self):
        """print representation of the Rectangle object"""
        return "[{}] {:d}/{:d}".format(self.__class__.__name__,
                                       self.__width, self.__height)

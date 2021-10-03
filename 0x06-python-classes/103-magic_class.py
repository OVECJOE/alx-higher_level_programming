#!/usr/bin/python3
"""A module that implements the bytecode found on the intranet
0x06-python-classes page, task 10"""
import math


class MagicClass:
    """A bytecode magic class"""

    def __init__(self, radius=0):
        """Initialize the attributes of this class objects"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """calculates the area of a square"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates the perimeter of the magic class"""
        return 2 * math.pi * self.__radius

#!/usr/bin/python3
"""Contains the BaseGeometry class"""


class BaseGeometry:
    """The base class for all geometry objects"""

    def area(self):
        """computes the area of this geometry"""
        raise Exception("area() is not implemented")

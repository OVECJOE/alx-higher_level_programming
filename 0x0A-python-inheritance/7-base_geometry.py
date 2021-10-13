#!/usr/bin/python3
"""A module that contains the BaseGeometry class"""


class BaseGeometry:
    """A base class for all geometry objects"""

    def area(self):
        """computes the area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates @value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

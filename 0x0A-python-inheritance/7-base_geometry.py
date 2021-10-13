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
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

#!/usr/bin/python3
"""Contains the function 'add_attribute'"""


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object if it's possible

    Args:
        obj (any): The object to be modified
        attr (str): The name of the attribute
        value (any): The value of the attribute
    """
    if "__dict__" in dir(obj) and type(obj.__dict__) is dict:
        obj.__dict__[attr] = value
    else:
        raise TypeError("can't add new attribute")

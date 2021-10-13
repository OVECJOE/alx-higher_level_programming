#!/usr/bin/python3
"""Contains a function that tests if an object inherits from a class"""


def inherits_from(obj, a_class):
    """returns True if @obj is an instance of a class that inherited
    from @a_class (directly or indirectly)"""
    return issubclass(type(obj), a_class) and (type(obj) is not a_class)

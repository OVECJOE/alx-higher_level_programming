#!/usr/bin/python3
"""Contains a function that returns True if an object is an instance of
a specified class"""


def is_same_class(obj, a_class):
    """returns True if @obj is instance of @a_class, else False"""
    return type(obj) is a_class

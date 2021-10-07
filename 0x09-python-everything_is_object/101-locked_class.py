#!/usr/bin/python3
"""A module that implements a LockedClass"""


class LockedClass:
    """defines a class that prevents the user from dynamically creating
    attributes, except if it is first_name"""
    __slots__ = ["first_name"]

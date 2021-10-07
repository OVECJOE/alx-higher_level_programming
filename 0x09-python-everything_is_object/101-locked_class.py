#!/usr/bin/python3
"""A module that implements a LockedClass"""


class LockedClass:
    """defines a class that prevents the user from dynamically creating
    attributes, except if it is first_name"""

    def __setattr__(self, key, value):
        """Sets a new attribute for the object"""
        if not hasattr(self, key) and key != "first_name":
            raise AttributeError("'LockedClass' object has"
                                 f" no attribute '{key}'")
        object.__setattr__(self, key, value)

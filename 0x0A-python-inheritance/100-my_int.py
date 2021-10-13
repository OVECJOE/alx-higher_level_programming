#!/usr/bin/python3
"""A module that contains a subclass of int"""


class MyInt(int):
    """Inherits from int"""

    def __eq__(self, value):
        """Works inversely to that of int"""
        return super().__ne__(value)

    def __ne__(self, value):
        """Works inversely to that of int"""
        return super().__eq__(value)

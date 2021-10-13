#!/usr/bin/python3
"""Contains MyList class that inherits from list"""


class MyList(list):
    """A subclass of the list class"""

    def print_sorted(self):
        """prints the list, but sorted (in ascending order)"""
        print(sorted(self))

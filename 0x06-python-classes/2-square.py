#!/usr/bin/python3
"""2-square.py - A module that contains a Square class"""


class Square:
    """defines a square by:

    - private instance variable: size
    - Instantiation with optional size
    """

    def __init__(self, size=0):
        """Initialize the instance properties"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

#!/usr/bin/python3
"""A module that declares a private instance variable: 'size'"""


class Square:
    """Square: A class that defines a square."""

    def __init__(self, size):
        """Constructor of the Square class

        Args:
            size (int): the size of the square
        """
        self.__size = size

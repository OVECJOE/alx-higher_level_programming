#!/usr/bin/python3
"""A module that contains a Square class"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A class that defines a square geometry"""

    def __init__(self, size):
        """Initialize a new square object"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """computes the area of the square"""
        return self.__size ** 2

#!/usr/bin/python3
"""A module that contains Square class"""


class Square:
    """Defines a square class"""

    def __init__(self, size=0):
        """Initializes the attributes for the square class"""
        self.size = size

    @property
    def size(self):
        """The getter method of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """The setter method of the size attribute"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2

    def __eq__(self, other):
        """Dunder method for == comparison"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Dunder method for != comparison"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Dunder method for > comparison"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Dunder method for >= comparison"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Dunder method for < comparison"""
        return self.area() < other.area()

    def __le__(self, other):
        """Dunder method for <= comparison"""
        return self.area() <= other.area()

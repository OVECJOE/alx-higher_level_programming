#!/usr/bin/python3
"""Implements a class Square that inherits from Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from the Rectangle class, a type of the Rectangle model"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the square object"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for the size"""
        return self.width

    @size.setter
    def size(self, size):
        """Setter method for the size"""
        self.width = size
        self.height = size

    def __str__(self):
        """Overrides the __str__ of parent class - Rectangle"""
        return "[{}] ({:d}) {:d}/{:d} - {:d}".format(
                type(self).__name__, self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assigns attributes to the square object

        Args:
            *args (ints): the list of no-keyworded arguments
            - id: the 1st argument
            - size: the 2nd argument
            - x: the 3rd argument
            - y: the 4th argument
            **kwargs (dict): a dict of key-value arguments
        """
        count = 0
        for arg in args:
            if count == 0:
                if arg is None:
                    self.__init(self.size, self.x, self.y, self.id)
                else:
                    self.id = arg
            elif count == 1:
                self.size = arg
            elif count == 2:
                self.x = arg
            elif count == 3:
                self.y = arg
            count += 1

        if kwargs:
            keys = ["id", "size", "x", "y"]
        for key, value in kwargs.items():
            if key in keys and keys.index(key) >= count:
                if key == keys[0]:
                    self.id = value
                elif key == keys[1]:
                    self.size = value
                elif key == keys[2]:
                    self.x = value
                elif key == keys[3]:
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of the object"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
        }

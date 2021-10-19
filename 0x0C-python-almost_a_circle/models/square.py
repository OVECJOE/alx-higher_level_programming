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
    def size(self, value):
        """Setter method for the size"""
        self.width = value
        self.height = value

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
        attrs = ('id', 'size', 'x', 'y')
        for key, val in zip(attrs, args):
            setattr(self, key, val)
        if (type(args) is None or len(args) == 0) and (type(kwargs) is dict):
            for key, val in kwargs.items():
                if key in attrs:
                    setattr(self, key, val)

    def to_dictionary(self):
        """returns the dictionary representation of the object"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
        }

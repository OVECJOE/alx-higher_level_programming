#!/usr/bin/python3
"""A module that implements the Rectangle class, a subclass of Base"""
from models.base import Base


class Rectangle(Base):
    """Inherits from Base class, models a rectangle object"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle object"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for the x attribute"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for the y attribute"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """computes the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints to stdout the Rectangle instance with the character '#'"""
        [print("") for i in range(self.__y)]
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """overrides the __str__ method
        Return:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                type(self).__name__, self.id, self.__x, self.__y,
                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updates the Rectangle class

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represents height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): assigns a key/value argument to attributes
        """
        count = 0
        for arg in args:
            if count == 0:
                if arg is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = arg
            elif count == 1:
                self.width = arg
            elif count == 2:
                self.height = arg
            elif count == 3:
                self.x = arg
            elif count == 4:
                self.y = arg
            count += 1

        for key, value in kwargs.items():
            temp = ["id", "width", "height", "x", "y"]
            if key in temp and temp.index(key) >= count:
                if key == temp[0]:
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    self.id = value
                elif key == temp[1]:
                    self.width = value
                elif key == temp[2]:
                    self.height = value
                elif key == temp[3]:
                    self.x = value
                elif key == temp[4]:
                    self.y = value

    def to_dictionary(self):
        """returns a dictionary representation of a Rectangle object"""
        result = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
        return result

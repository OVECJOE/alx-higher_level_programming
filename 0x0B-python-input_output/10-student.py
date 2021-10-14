#!/usr/bin/python3
"""Contains a Student class"""


class Student:
    """defines a student object"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if type(attrs) is list and all(type(s) is str for s in attrs):
            res = {}
            for key in attrs:
                if key in self.__dict__:
                    res[key] = self.__dict__[key]
            return res
        else:
            return self.__dict__

#!/usr/bin/python3
"""A module that contains a function that prints the full name of a person"""


def say_my_name(first_name, last_name=""):
    """Says the full name of a person

    Args:
        first_name (str): the first name provided
        last_name (str): the last name provided - optional

    Format of output:
        My name is <first_name> <last_name>

    Exceptions:
        TypeError - If first_name or last_name is not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")

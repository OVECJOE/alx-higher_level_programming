#!/usr/bin/python3
"""contains the function write_file(...)"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and
    returns the number of characters"""
    with open(filename, "w") as f:
        no_of_chars = f.write(text)
    return no_of_chars

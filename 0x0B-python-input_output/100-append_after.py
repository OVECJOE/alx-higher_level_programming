#!/usr/bin/python3
"""Contains 'append_after(...)' which appends a text of line to a file"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text after each line containing a specific string

    Args:
        filename (str): the name of the file
        search_string (str): the string to be searched within the file
        new_string (str): the new string to be inserted

    Return: None
    """
    text = ""

    with open(filename, encoding="utf-8") as rf:
        for line in rf:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

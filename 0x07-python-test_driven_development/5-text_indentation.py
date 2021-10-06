#!/usr/bin/python3
"""Contains a function that indent text passed as argument"""


def text_indentation(text):
    """prints a text with 2 new lines after each of '.', '?' and ':'

    Args:
        text (str): the passed string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i, j = 0, 0
    for a, c in enumerate(text):
        if c in ('.', ':', '?'):
            print(text[i:j+1], end="\n\n")
            i = j + 2
        else:
            if j == len(text) - 1:
                print(text[i:], end="")
        j += 1

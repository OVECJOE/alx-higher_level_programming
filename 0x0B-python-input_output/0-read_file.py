#!/usr/bin/python3
"""Contains read_file(...) function"""


def read_file(filename=""):
    """reads a text file (UTF-8) and print it to stdout"""
    with open(filename, encoding="utf-8") as f:
        for line in f.readlines():
            print(line.rstrip())

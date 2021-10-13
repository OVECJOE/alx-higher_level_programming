#!/usr/bin/python3
"""A module that contains the function from_json_string(...)"""
import json


def from_json_string(my_str):
    """converts a json string to a python object"""
    return json.loads(my_str)

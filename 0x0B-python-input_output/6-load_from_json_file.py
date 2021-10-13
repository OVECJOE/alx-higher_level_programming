#!/usr/bin/python3
"""A module that contains the function 'load_from_json_file(...)'"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy = a_dictionary.copy()
    for item in copy.items():
        if item[1] == value:
            del a_dictionary[item[0]]
    del copy
    return a_dictionary

#!/usr/bin/python3
"""Defines a peak-finding algorithm"""


def find_peak(ints_list):
    """Returns a peak in a list of unsorted integers"""
    if not ints_list:
        return None

    length = len(ints_list)
    if length == 1 or length == 2:
        return max(ints_list)

    midpoint = int(length / 2)
    peak = ints_list[midpoint]
    if ints_list[midpoint - 1] < peak > ints_list[midpoint + 1]:
        return peak
    elif peak < ints_list[midpoint - 1]:
        return find_peak(ints_list[:midpoint])
    else:
        return find_peak(ints_list[midpoint + 1:])

#!/usr/bin/python3
"""Contains a function called pascal_triangle(...)"""


def pascal_triangle(n):
    """returns a list of lists of integers representing pascal's triangle
    of n"""
    result = []

    if n <= 0:
        return []

    for i in range(n):
        if len(result) in [0, 1]:
            result.append([1] * (len(result) + 1))
            continue
        temp = [1, 1]
        for i in range(len(result[-1]) - 1):
            temp.insert(i+1, result[-1][i] + result[-1][i+1])
        result.append(temp)
    return result

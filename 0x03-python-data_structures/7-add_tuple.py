#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a[:2] + (0,) * (2 - len(tuple_a))
    b = tuple_b[:2] + (0,) * (2 - len(tuple_b))
    result = [x + y for x, y in zip(a, b)][:2]
    return tuple(result)

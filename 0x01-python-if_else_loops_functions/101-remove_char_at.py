#!/usr/bin/python3
def remove_char_at(str, n):
    copy = []
    for i, j in enumerate(str):
        if i == n:
            continue
        copy.append(j)

    return "".join(copy)

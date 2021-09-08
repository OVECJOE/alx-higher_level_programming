#!/usr/bin/python3
for i, c in enumerate(range(122, 96, -1)):
    print("{:c}".format(c - 32 if i % 2 else c), end="")

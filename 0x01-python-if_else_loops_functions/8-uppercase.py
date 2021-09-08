#!/usr/bin/python3
def uppercase(str):
    for c in str:
        isupper = ord(c) >= 65 and ord(c) <= 90
        isnumeric = ord(c) >= 48 and ord(c) <= 57
        print("{:c}".format(ord(c) if isupper or isnumeric else ord(c) - 32),
              end="")
    print()

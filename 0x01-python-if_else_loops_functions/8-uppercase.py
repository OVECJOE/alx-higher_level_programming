#!/usr/bin/python3
def uppercase(str):
    for c in str:
        islower = ord(c) >= 97 and ord(c) <= 122
        print("{:c}".format(ord(c) - 32 if islower else ord(c)), end="")
    print()

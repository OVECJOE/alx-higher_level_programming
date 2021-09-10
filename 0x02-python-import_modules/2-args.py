#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv) - 1
    print("{:d} argument".format(argc), end="")
    if (argc):
        print("{}".format(":" if argc == 1 else "s:"))
    else:
        print("s.")
    for i in range(1, argc + 1):
        print("{:d}: {}".format(i, argv[i]))

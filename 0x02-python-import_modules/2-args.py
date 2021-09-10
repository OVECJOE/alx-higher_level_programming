#!/usr/bin/python3
from sys import argv

argc = len(argv) - 1
print("{:d} arguments{}".format(argc, ":" if argc else "."))
if argc:
    for i in range(1, argc + 1):
        print("{:d}: {}".format(i, argv[i]))

#!/usr/bin/python3
from sys import argv
import calculator_1 as calc
argc = len(argv) - 1
if argc != 3:
    print("Usage: {} <a> <operator> <b>".format(argv[0]))
    exit(1)
a = int(argv[1])
operator = argv[2]
b = int(argv[3])

if operator == "+":
    result = calc.add(a, b)
elif operator == "-":
    result = calc.sub(a, b)
elif operator == "*":
    result = calc.mul(a, b)
elif operator == "/":
    result = calc.div(a, b)
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
print("{:d} {} {:d} = {:d}".format(a, operator, b, result))

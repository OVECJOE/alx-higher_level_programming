#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        number %= 10
        print(number, end="")
    else:
        number = (number * -1) % 10
        print(number, end="")
    return number

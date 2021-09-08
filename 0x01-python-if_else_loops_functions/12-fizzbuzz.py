#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif not i % 3:
            print("Fizz", end=" ")
        elif not i % 5:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

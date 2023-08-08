#!/usr/bin/python3
# 12-fizzbuzz.py

"""This Function Print the numbers from 1 to 100 separated by a space.
    For multiples of three, print Fizz instead of the number.
    For multiples of five, print Buzz instead of the number.
    For multiples of three and five, print FizzBuzz instead of the number.
    """
def fizzbuzz():
    for six in range(1, 101):
        if six % 3 == 0 and six % 5 == 0:
            print("FizzBuzz ", end="")
        elif six % 3 == 0:
            print("Fizz ", end="")
        elif six % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(six), end="")

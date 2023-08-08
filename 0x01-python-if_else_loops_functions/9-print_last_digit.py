#!/usr/bin/python3

"""This Function Print the last digit of a number and return it."""
"""@number: Is a number to be Checked."""

def print_last_digit(number):
    print(abs(number) % 10, end="")
    return (abs(number) % 10)

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
one = abs(number) % 10
if number < 0:
    one = -one
print("Last one of {} is {} and is ".format(number, one), end="")
if one > 5:
    print("greater than 5")
elif one == 0:
    print("0")
else:
    print("less than 6 and not 0")

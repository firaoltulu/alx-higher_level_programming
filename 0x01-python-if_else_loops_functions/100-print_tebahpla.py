#!/usr/bin/python3

"""Print the alphabet in reverse order alternating upper- and lower-case."""
one = 0
for two in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(two - one)), end="")
    one = 32 if one == 0 else 0

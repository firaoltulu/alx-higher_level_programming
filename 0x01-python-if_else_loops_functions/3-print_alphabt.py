#!/usr/bin/python3

"""This Program Print all alphabet except q and e in lowercase not new line at the end."""
for three in range(97, 123):
    if chr(three) != 'q' and chr(three) != 'e':
        print("{}".format(chr(three)), end="")

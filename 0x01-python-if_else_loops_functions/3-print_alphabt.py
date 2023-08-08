#!/usr/bin/python3

"""This Program Print all alphabet except q and e in lowercase not new line at the end."""
for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")

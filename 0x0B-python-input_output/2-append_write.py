#!/usr/bin/python3
"""
This function that appends a string
"""


def append_write(filename="", text=""):
    """This returns the number of characters added:"""
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)

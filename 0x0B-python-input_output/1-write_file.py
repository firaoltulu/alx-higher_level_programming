#!/usr/bin/python3
"""
This Contains the function "wrtie_file."
"""


def write_file(filename="", text=""):
    """This returns the number of chars written to "filename" from "text". """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)

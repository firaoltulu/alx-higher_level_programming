#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""

def text_indentation(text):
    """This splits a text into lines along "?", ":", "." followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    four = 0
    for one in text:
        if four == 0:
            if one == ' ':
                continue
            else:
                four = 1
        if four == 1:
            if one == '?' or one == '.' or one == ':':
                print(one)
                print()
                four = 0
            else:
                print(one, end="")


#!/usr/bin/python3

"""This Program Print all names
   defined by hidden_4 module."""
if __name__ == "__main__":
    import hidden_4

    three = dir(hidden_4)
    for four in three:
        if four[:2] != "__":
            print(four)

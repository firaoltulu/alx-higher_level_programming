#!/usr/bin/python3

"""This Program Print the number of and
    list of arguments passed."""
if __name__ == "__main__":
    import sys

    one = len(sys.argv) - 1
    if one == 0:
        print("0 arguments.")
    elif one == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(one))
    for two in range(one):
        print("{}: {}".format(two + 1, sys.argv[two + 1]))

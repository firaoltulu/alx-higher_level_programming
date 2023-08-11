#!/usr/bin/python3

"""This Program Print the addition of all arguments."""
if __name__ == "__main__":
    import sys

    one = sys.argv[1:]
    def custom_add(*two):
        total = sum(int(arg) for arg in two)
        return total

    result = custom_add(*one)
    print("{}".format(result))

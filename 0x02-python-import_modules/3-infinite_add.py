#!/usr/bin/python3

"""This Program Print the addition of all arguments."""
if __name__ == "__main__":
    import sys

    def custom_add(*arguments):
        total = sum(int(arg) for arg in arguments)
        return total

    arguments = sys.argv[1:]
    result = custom_add(*arguments)
    print("{}".format(result))

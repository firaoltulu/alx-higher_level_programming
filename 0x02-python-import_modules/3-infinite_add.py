#!/usr/bin/python3

"""This Program Print the addition of all arguments."""
if __name__ == "__main__":
    import sys

    arguments = sys.argv[1:]
    def custom_add(*arguments):
        total = sum(int(arg) for arg in arguments)
        return total



    result = custom_add(*arguments)
    print("{}".format(result))

#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    one = 0
    for two in range(x):
        try:
            print("{}".format(my_list[two]), end="")
            one += 1
        except IndexError:
            break
    print("")
    return (one)

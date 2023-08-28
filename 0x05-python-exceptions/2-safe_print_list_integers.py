#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    one = 0
    for two in range(0, x):
        try:
            print("{:d}".format(my_list[two]), end="")
            one += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (one)

#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        one = a / b
    except (TypeError, ZeroDivisionError):
        one = None
    finally:
        print("Inside result: {}".format(one))
    return (one)

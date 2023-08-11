#!/usr/bin/python3

"""This Program Handle basic arithmetic operations."""
if __name__ == "__main__":
    import sys
    from calculator_1 import add as loc_add, sub as loc_sub, mul as loc_mul, div as loc_div 
    
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    one = {"+": loc_add, "-": loc_sub, "*": loc_mul, "/": loc_div}
    if sys.argv[2] not in list(one.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, one[sys.argv[2]](a, b)))

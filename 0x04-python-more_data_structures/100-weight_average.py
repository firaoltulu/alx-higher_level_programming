#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    one = 0
    two = 0

    for three in my_list:
        one += three[0] * three[1]
        two += three[1]

    return (one / two)

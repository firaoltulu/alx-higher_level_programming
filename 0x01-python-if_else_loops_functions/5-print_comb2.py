#!/usr/bin/python3
for five in range(0, 100):
    if five == 99:
        print("{}".format(five))
    else:
        print("{:02}".format(five), end=", ")

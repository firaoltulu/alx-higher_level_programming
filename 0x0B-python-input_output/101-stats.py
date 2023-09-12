#!/usr/bin/python3
"""
This reads stdin line by line and computes metrics.
"""
import sys

one = 0
two = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
three = 0
try:
    for four in sys.stdin:
        five = four.split()
        if len(five) >= 2:
            six = three
            if five[-2] in two:
                two[five[-2]] += 1
                three += 1
            try:
                one += int(five[-1])
                if six == three:
                    three += 1
            except FileNotFoundError:
                if six == three:
                    continue
        if three % 10 == 0:
            print("File size: {:d}".format(one))
            for seven, eight in sorted(two.items()):
                if eight:
                    print("{:s}: {:d}".format(seven, eight))
    print("File size: {:d}".format(one))
    for seven, eight in sorted(two.items()):
        if eight:
            print("{:s}: {:d}".format(seven, eight))

except KeyboardInterrupt:
    print("File size: {:d}".format(one))
    for seven, eight in sorted(two.items()):
        if eight:
            print("{:s}: {:d}".format(seven, eight))

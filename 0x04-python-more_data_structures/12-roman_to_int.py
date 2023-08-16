#!/usr/bin/python3
def local_subtract(one):
    two = 0
    three = max(one)

    for n in one:
        if three > n:
            two += n

    return (three - two)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    two = list(roman_numbers.keys())

    four = 0
    three = 0
    one = [0]

    for five in roman_string:
        for six in two:
            if six == five:
                if roman_numbers.get(five) <= three:
                    four += local_subtract(one)
                    one = [roman_numbers.get(five)]
                else:
                    one.append(roman_numbers.get(five))

                three = roman_numbers.get(five)

    four += local_subtract(one)

    return (four)

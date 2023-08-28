#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):

    one = []
    for two in range(0, list_length):
        try:
            three = my_list_1[two] / my_list_2[two]
        except TypeError:
            print("wrong type")
            three = 0
        except ZeroDivisionError:
            print("division by 0")
            three = 0
        except IndexError:
            print("out of range")
            three = 0
        finally:
            one.append(three)
    return (one)

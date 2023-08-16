#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda one: replace if one == search else one, my_list))
    return (new_list)

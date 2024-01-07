#!/usr/bin/python3
def max_integer(my_list=[]):
    max_int = 0
    i = 0
    if len(my_list) == 0:
        max_int = None
    while i < len(my_list):

        if max_int < my_list[i]:
            max_int = my_list[i]
        i += 1
    return max_int

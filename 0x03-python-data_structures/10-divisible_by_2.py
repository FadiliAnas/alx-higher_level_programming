#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    i = 0
    x = []
    while i < len(my_list):
        if my_list[i] % 2 == 0:
            x.append(True)
        elif my_list[i] % 2 != 0:
            x.append(False)
        i += 1
    return x

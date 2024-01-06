#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return None
    elif idx > lenght(my_list[:]) - 1:
        return None
    else:
        new_my_list = my_list
        new_my_list[idx] = element
        return new_my_list

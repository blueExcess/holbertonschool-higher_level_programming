#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    ll = len(my_list)
    if idx > ll or idx < 0:
        return my_list
    my_list[idx] = element
    return my_list

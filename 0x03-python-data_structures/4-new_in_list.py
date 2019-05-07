#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    ll = len(my_list)
    newList = my_list[:]
    if idx >= ll or idx < 0:
        return newList
    newList[idx] = element
    return newList

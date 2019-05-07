#!/usr/bin/python3
def element_at(my_list, idx):
    ll = len(my_list)
    if idx > ll or idx < 0:
        return None
    return my_list[idx]

#!/usr/bin/python3
def weight_average(my_list=[]):
    isum, weight = 0, 0
    if my_list is None or len(my_list) < 1:
        return 0
    for x in my_list:
        isum += (x[0] * x[1])
    for x in my_list:
        weight += x[1]
    return isum / weight

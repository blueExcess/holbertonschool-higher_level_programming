#!/usr/bin/python3
def complex_delete(d, value):
    for k, v in d.items():
        if v == value:
            del d[k]
            return complex_delete(d, value)
    return d

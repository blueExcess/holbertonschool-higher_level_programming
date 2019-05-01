#!/usr/bin/python3
# mimic upper()


def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            value = ord(i) - 32
        else:
            value = ord(i)
        print("{:c}".format(value), end="")
    else:
        print()

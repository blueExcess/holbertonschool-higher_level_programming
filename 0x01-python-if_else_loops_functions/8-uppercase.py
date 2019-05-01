#!/usr/bin/python3
# mimic upper()
def uppercase(str):
    for i in str:
        if ord(i) < 97 and ord(i) > 122:
            value = ord(i)
        else:
            value = ord(i) - 32
        print("{:c}".format(value), end="")
    else:
        print()

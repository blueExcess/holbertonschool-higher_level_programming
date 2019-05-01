#!/usr/bin/python3
# print alphabet backwards alternating caps and not
# e.g. zYxW...
for i in range(122, 96, -1):
    print(("{:c}".format(i) if i % 2 == 0 else "{:c}".format(i - 32)), end="")

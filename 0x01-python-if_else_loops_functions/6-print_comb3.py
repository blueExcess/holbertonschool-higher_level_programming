#!/usr/bin/python3
# print out series of numbers
for i in range(1, 10):
        for x in range(i, 10):
                if (i-1) == 8 and x == 9:
                        print("{:d}{:d}".format((i-1), x))
                else:
                        print("{:d}{:d}, ".format((i-1), x), end="")

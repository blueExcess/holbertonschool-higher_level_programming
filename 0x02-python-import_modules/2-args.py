#!/usr/bin/python3

from sys import argv
if __name__ == '__main__':
    count = 0
    if len(argv) == 1:
        print("0 arguments.")
        exit()
    narg = len(argv) - 1
    if len(argv) == 2:
        print('{} argument:'.format(narg))
    else:
        print('{} arguments:'.format(narg))
    for x in argv:
        count += 1
        if count == 1:
            continue
        print('{}: {}'.format(count - 1, x))

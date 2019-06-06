#!/usr/bin/python3
"""2. Read out n number of lines."""


def read_lines(filename="", nb_lines=0):
    """Return given number of lines from indicated file."""
    lineNo = 0
    with open(filename) as f:
        for line in f:
            lineNo += 1
            if lineNo <= nb_lines or nb_lines <= 0:
                print(line, end="")

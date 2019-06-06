#!/usr/bin/python3
"""1. Count number of lines."""


def number_of_lines(filename=""):
    """Count number of lines in a file."""
    count = 0
    with open(filename) as f:
        for line in f:
            count += 1
    return count

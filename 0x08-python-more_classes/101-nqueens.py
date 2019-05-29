#!/usr/bin/python3
"""module for function to find solution to n queens problem."""
from sys import argv


def queens():
    """Find solution to N Queens problem."""
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not isinstance(argv[1], int):
        print('N must be a number')
        exit(1)
    elif argv[1] < 4:
        print('N must be at least 4')
        exit(1)

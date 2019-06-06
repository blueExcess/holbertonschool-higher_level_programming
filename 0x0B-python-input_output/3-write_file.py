#!/usr/bin/python3
"""3. Write string to text file and return num of chars written."""


def write_file(filename="", text=""):
    """Write string to file and return num of chars written."""
    with open(filename, 'wt') as f:
        return f.write(text)

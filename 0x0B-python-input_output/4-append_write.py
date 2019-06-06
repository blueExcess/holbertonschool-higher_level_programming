#!/usr/bin/python3
"""4. append string at end of text file."""


def append_write(filename="", text=""):
    """Append text to end of file and return num of chars added."""

    with open(filename, mode='a') as f:
        return f.write(text)

#!/usr/bin/python3
"""Mod doc goes here."""


def read_file(filename=""):
    """read a file and print to stdout."""
    with open(filename) as f:
        print(f.read(), end='')

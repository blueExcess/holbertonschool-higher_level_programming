#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, x in enumerate(row):
            print("{:d}".format(x), end="" if i == len(row) - 1 else " ")
        print()

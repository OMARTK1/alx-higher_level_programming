#!/usr/bin/python3
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    for row in matrix:
        for idx, num in enumerate(row):
            print("{:d}".format(num), end="")
            if idx < len(row) - 1:
                print(" ", end="")
        print()

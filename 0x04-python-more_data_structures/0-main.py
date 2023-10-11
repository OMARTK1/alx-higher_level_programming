#!/usr/bin/python3
import importlib

matrix_module = importlib.import_module('0-square_matrix_simple')
square_matrix_simple = matrix_module.square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

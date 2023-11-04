#!/usr/bin/python3
"""Defining a function that divide all elements in matrix."""


def matrix_divided(matrix, div):
    """Defining a function that divide all elements in matrix..

    Return:
        the new matrix that represent the result of the divided elements.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(R, list) for R in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [n for R in matrix for n in R])):
                raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(R) == len(matrix[0]) for R in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), R)) for R in matrix])

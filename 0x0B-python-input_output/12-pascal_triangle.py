#!/usr/bin/python3
"""
Module for Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the given number of rows.

    Args:
        n (int): Number of rows in Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        row = [1]
        if triangle[-1]:
            row.extend([sum(pair) for pair in zip(triangle[-1], triangle[-1][1:])])
            row.append(1)
        triangle.append(row)

    return triangle

if __name__ == "__main__":
    n = 5
    result = pascal_triangle(n)
    for row in result:
        print(row)

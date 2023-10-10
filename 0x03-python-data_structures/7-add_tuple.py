#!/usr/bin/python3
# 7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples and returns a new tuple."""
    # Take the first two elements from each tuple, or use 0 if not available
    a = tuple_a[0] if len(tuple_a) > 0 else 0
    b = tuple_a[1] if len(tuple_a) > 1 else 0
    c = tuple_b[0] if len(tuple_b) > 0 else 0
    d = tuple_b[1] if len(tuple_b) > 1 else 0

    # Calculate the sum of the first elements
    # and the sum of the second elements
    sum_first = a + c
    sum_second = b + d

    # Return the new tuple
    return (sum_first, sum_second)

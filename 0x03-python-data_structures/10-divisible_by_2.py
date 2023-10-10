#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list and returns a new list
    with True or False."""
    return [num % 2 == 0 for num in my_list]

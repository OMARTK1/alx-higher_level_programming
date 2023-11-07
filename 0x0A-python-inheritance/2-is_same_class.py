#!/usr/bin/python3
"""
Module containing a function is_same_class that checks if an object is an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Args:
        obj (object): Input object.
        a_class (type): Specified class.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) == a_class

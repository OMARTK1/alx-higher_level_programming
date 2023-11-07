#!/usr/bin/python3
"""
Module containing a function is_kind_of_class that checks
if an object is an instance of, or inherits from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or inherits from, a specified class.

    Args:
        obj (object): Input object.
        a_class (type): Specified class.

    Returns:
        bool: True if obj is an instance of or inherits
        from a_class, False otherwise.
    """
    return isinstance(obj, a_class)

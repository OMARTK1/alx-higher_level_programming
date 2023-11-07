#!/usr/bin/python3
"""
Module containing a function inherits_from that checks
if an object is a subclass of a specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is a subclass of a specified class.

    Args:
        obj (object): Input object.
        a_class (type): Specified class.

    Returns:
        bool: True if obj is a subclass of a_class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

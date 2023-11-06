#!/usr/bin/python3
"""
Module containing a function that returns the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj (object): Input object.

    Returns:
        list: List of attributes and methods of the object.
    """
    return dir(obj)

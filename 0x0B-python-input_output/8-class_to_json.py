#!/usr/bin/python3
"""
Module for converting a class instance to a JSON representation
"""


def class_to_json(obj):
    """
    Converts a class instance to a JSON representation.

    Args:
        obj (obj): Python class instance.

    Returns:
        dict: Dictionary representation of the object.

    """
    return obj.__dict__

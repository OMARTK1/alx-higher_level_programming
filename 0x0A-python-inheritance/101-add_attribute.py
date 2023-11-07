#!/usr/bin/python3
"""
Module containing the add_attribute function.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj (object): The object to add the attribute to.
        name (str): The name of the attribute.
        value (any): The value of the attribute.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if hasattr(obj, "__dict__") or hasattr(obj, "__slots__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")

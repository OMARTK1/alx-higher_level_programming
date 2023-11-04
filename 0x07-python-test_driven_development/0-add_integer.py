#!/usr/bin/python3
"""Defining an int addition function."""


def add_integer(a, b=98):
    """Return an integer: addition of a and b

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If a and b are not an integer or a float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

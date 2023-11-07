#!/usr/bin/python3
"""
Module containing a class BaseGeometry with methods area and integer_validator.
"""


class BaseGeometry:
    """
    Class BaseGeometry with methods area() and integer_validator(name, value).
    """
    def area(self):
        """
        Raises an Exception with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value.

        Args:
            name (str): Name of the value.
            value (int): Value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

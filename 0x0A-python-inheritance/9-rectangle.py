#!/usr/bin/python3
"""
Module containing a class Rectangle that inherits from BaseGeometry.
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


class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the rectangle description [Rectangle] <width>/<height>.

        Returns:
            str: Rectangle description.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

#!/usr/bin/python3
"""Defining the class"""


class Rectangle:
    """class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Construct the rectangle.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """sets the width of the rectangle.

        Returns:
            width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """gets the width of the rectangle.

        Args:
            value (integer): The width of the rectangle.

        Raises:
            TypeError: If the width is not an int.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """sets the height of the rectangle.

        Returns:
            height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """gets the height of the rectangle.

        Args:
            value (integer): height of the rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

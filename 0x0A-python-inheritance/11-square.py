#!/usr/bin/python3
"""
Module containing the Square class inheriting from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Square class inheriting from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): Size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the square description.

        Returns:
            str: Square description.
        """
        return "[Square] {}/{}".format(self.__width, self.__height)

#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initializes the square with a given size"""
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' characters"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

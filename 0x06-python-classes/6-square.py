#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            sqr_size (int): The size of the new square.
            sqr_position (int, int): The position of the new square.
        """
        self.sqr_size = size
        self.sqr_position = position

    @property
    def sqr_size(self):
        """Get/set the current size of the square."""
        return self.__size

    @sqr_size.setter
    def sqr_size(self, value):
        if not isinstance(value, int):
            raise TypeError("sqr_size must be an integer")
        elif value < 0:
            raise ValueError("sqr_size must be >= 0")
        self.__size = value

    @property
    def sqr_position(self):
        """Get/set the current position of the square."""
        return self.__position

    @sqr_position.setter
    def sqr_position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("sqr_position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for _ in range(0, self.__position[1])]
        for _ in range(0, self.__size):
            [print(" ", end="") for _ in range(0, self.__position[0])]
            [print("#", end="") for _ in range(0, self.__size)]
            print("")

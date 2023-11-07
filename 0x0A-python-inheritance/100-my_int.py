#!/usr/bin/python3
"""
Module containing the MyInt class.
"""


class MyInt(int):
    """
    MyInt class that inherits from int.
    """
    def __eq__(self, other):
        """
        Overrides the equality operator.

        Args:
            other (int): The other integer to compare.

        Returns:
            bool: True if self is not equal to other, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator.

        Args:
            other (int): The other integer to compare.

        Returns:
            bool: True if self is equal to other, False otherwise.
        """
        return super().__eq__(other)

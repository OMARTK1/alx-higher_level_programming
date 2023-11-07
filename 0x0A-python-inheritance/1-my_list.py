#!/usr/bin/python3
"""
Module containing a class MyList that inherits from list.
"""


class MyList(list):
    """
    Class MyList that inherits from list. Overrides print_sorted method.
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.
        """
        print(sorted(self))

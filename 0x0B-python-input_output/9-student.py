#!/usr/bin/python3
"""
Module for representing a student as a JSON object
"""


class Student:
    """
    Represents a student.

    Attributes:
        first_name (str): First name of the student.
        last_name (str): Last name of the student.
        age (int): Age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.

        Returns:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Converts the student object to a JSON representation.

        Args:
            None

        Returns:
            dict: JSON representation of the student object.

        """
        return self.__dict__

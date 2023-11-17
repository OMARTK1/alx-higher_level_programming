#!/usr/bin/python3
"""
Module for representing a student as a JSON object with attribute filtering
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

    def to_json(self, attrs=None):
        """
        Converts the student object to a JSON representation
        with attribute filtering.

        Args:
            attrs (list): List of attribute names to include
            in the JSON representation.

        Returns:
            dict: JSON representation of the student object.

        """
        if attrs is None or not all(isinstance(attr, str) for attr in attrs):
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
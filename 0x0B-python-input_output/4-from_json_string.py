#!/usr/bin/python3
"""
Module for converting a JSON string to a Python object.
"""
import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
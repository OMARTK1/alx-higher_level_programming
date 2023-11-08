#!/usr/bin/python3
"""
Module for saving objects to a JSON file
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.

    Args:
        my_obj (obj): Python object to be serialized.
        filename (str): Name of the file to save the JSON representation.

    Returns:
        None
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)

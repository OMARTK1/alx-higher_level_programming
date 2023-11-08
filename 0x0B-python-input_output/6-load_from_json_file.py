#!/usr/bin/python3
"""
Module for loading an object from a JSON file
"""

import json

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): Name of the JSON file.

    Returns:
        obj: Python object reconstructed from the JSON file.

    Raises:
        FileNotFoundError: If the file specified does not exist.

    """
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    import sys

    filename = sys.argv[1]
    obj = load_from_json_file(filename)
    print(obj)
    print(type(obj))

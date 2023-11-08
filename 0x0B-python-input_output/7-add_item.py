#!/usr/bin/python3
"""
Module for loading, adding arguments, and saving to a JSON file
"""

import sys


def load_add_save():
    """
    Loads, adds arguments to a list, and saves them to a JSON file.

    Args:
        None

    Returns:
        None
    """
    try:
        with open("add_item.json", mode='r', encoding='utf-8') as file:
            my_list = json.load(file)
    except FileNotFoundError:
        my_list = []
    my_list.extend(sys.argv[1:])
    with open("add_item.json", mode='w', encoding='utf-8') as file:
        json.dump(my_list, file)

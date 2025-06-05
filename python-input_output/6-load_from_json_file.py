#!/usr/bin/python3

"""
This module provides a function that creates an object from a JSON file.

Functions:
    load_from_json_file(filename): Creates an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)

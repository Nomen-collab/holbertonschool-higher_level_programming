#!/usr/bin/python3
"""
Module: 5-save_to_json_file
This module provides a function to write an object to a text file
using its JSON representation.
"""
import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The Python object to be serialized and saved.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

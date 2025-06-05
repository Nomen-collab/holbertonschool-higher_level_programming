#!/usr/bin/python3

"""
This module provides a function that returns the dictionary
description with simple data structure (list, dictionary, string,
integer, and boolean) for JSON serialization of an object.

Functions:
    class_to_json(obj): Returns the dictionary description of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON
    serialization of an object.

    Args:
        obj (object): The object to serialize.

    Returns:
        dict: The dictionary description of the object.
    """
    return obj.__dict__

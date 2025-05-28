#!/usr/bin/python3
"""
This module defines a function `lookup` that returns the list of available
attributes and methods of an object.

The `lookup` function:
- Takes an object as an argument.
- Returns a list of strings representing the attributes and methods
of the object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings representing the attributes and
        methods of the object.
    """
    return dir(obj)

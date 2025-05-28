#!/usr/bin/python3
"""
This module defines a function `is_same_class` that checks if an object
is exactly an instance of a specified class.

The `is_same_class` function:
- Takes an object and a class as arguments.
- Returns True if the object is exactly an instance of the specified
class; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified
    class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is exactly an instance of a_class, otherwise
        False.
    """
    return type(obj) is a_class

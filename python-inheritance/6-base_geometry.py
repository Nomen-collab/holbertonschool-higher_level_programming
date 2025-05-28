#!/usr/bin/python3
"""
This module defines a class `BaseGeometry`.

The `BaseGeometry` class:
- Serves as a base for geometry-related classes.
- Includes a public instance method `area` that raises an Exception
with the message 'area() is not implemented'.
"""


class BaseGeometry:
    """
    A class that serves as a base for geometry-related classes.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

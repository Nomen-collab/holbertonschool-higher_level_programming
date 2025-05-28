#!/usr/bin/python3
"""
This module defines a class `BaseGeometry`.

The `BaseGeometry` class:
- Serves as a base for geometry-related classes.
- Includes a public instance method `area` that raises an Exception
  with the message 'area() is not implemented'.
- Includes a public instance method `integer_validator` that validates
  the value.
"""


class BaseGeometry:
    """
    A class that serves as a base for geometry-related classes.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.

        This method is intended to be overridden in subclasses to provide
        the area calculation for specific geometric shapes.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name=None, value=None):
        """
        Validates the value.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer or is a boolean.
            ValueError: If value is less or equal to 0.
        """
        if isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

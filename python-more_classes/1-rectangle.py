#!/usr/bin/python3
"""
This module defines a class Rectangle that represents a rectangle.

The Rectangle class includes:
- Private instance attributes `__width` and `__height` to store
  the dimensions of the rectangle.
- A constructor to initialize the width and height with validation.
- Properties to retrieve the width and height.
- Property setters to set the width and height with validation.
"""


class Rectangle:
    """
    This class represents a rectangle with private width and height attributes.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle with a given width and height.

        Args:
            width (int): The width of the rectangle. Must be an integer >= 0.
            height (int): The height of the rectangle. Must be an integer >= 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width  # Use the setter for validation
        self.height = height  # Use the setter for validation

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle with validation.

        Args:
            value (int): The width of the rectangle. Must be an integer >= 0.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle with validation.

        Args:
            value (int): The height of the rectangle.
            Must be an integer >= 0.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

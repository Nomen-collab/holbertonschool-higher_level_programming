#!/usr/bin/python3
"""
This module defines a class `Square` that inherits from `Rectangle`.

Classes:
    Square: A class to represent a square.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class to represent a square, inheriting from Rectangle.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"

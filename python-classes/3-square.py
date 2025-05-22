#!/usr/bin/python3

"""Defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes a new square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size * self.__size

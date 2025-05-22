#!/usr/bin/python3
"""Define a square"""


class Square:
    """Square with size"""

    def __init__(self, size=0):
        """Initialize square

        Args:
            size (int): Size of square
        """
        self.size = size

    @property
    def size(self):
        """Get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size

        Args:
            value (int): Size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of square

        Returns:
            Area of square
        """
        return self.__size * self.__size

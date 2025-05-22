#!/usr/bin/python3
"""Define a square"""


class Square:
    """Square with size and position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square

        Args:
            size (int): Size of square
            position (tuple): Position of square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position

        Args:
            value (tuple): Position of square
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area of square

        Returns:
            Area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """Print square"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

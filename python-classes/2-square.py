#!/usr/bin/python3

"""Defines a square"""


class Square:
    """Defines a square based on 1-square.py"""

    def __init__(self, size=0):
        """Initializes the square"""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

#!/usr/bin/python3
"""
This module defines a class `MyList` that inherits from
the built-in `list` class.

The `MyList` class:
- Inherits from the built-in `list` class.
- Provides a method `print_sorted` that prints the list in sorted order.
"""


class MyList(list):
    """
    A class that inherits from list and provides a method to print
    the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        Assumes that all elements of the list are of type int.
        """
        print(sorted(self))

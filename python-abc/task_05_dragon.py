#!/usr/bin/env python3
"""
This module defines mixin classes `SwimMixin` and `FlyMixin`, and
a `Dragon` class that inherits from both.

Classes:
    SwimMixin: A mixin class that provides swimming capability.
    FlyMixin: A mixin class that provides flying capability.
    Dragon: A class to represent a dragon, inheriting from both
    SwimMixin and FlyMixin.
"""


class SwimMixin:
    """
    A mixin class that provides swimming capability.

    Methods:
        swim: Prints a message indicating that the creature swims.
    """

    def swim(self):
        """
        Print a message indicating that the creature swims.
        """
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class that provides flying capability.

    Methods:
        fly: Prints a message indicating that the creature flies.
    """

    def fly(self):
        """
        Print a message indicating that the creature flies.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class to represent a dragon, inheriting from both SwimMixin and FlyMixin.

    Methods:
        roar: Prints a message indicating that the dragon roars.
    """

    def roar(self):
        """
        Print a message indicating that the dragon roars.
        """
        print("The dragon roars!")

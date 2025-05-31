#!/usr/bin/env python3
"""
This module defines an abstract base class `Animal` and its
subclasses `Dog` and `Cat`.

Classes:
    Animal: An abstract base class for animals.
    Dog: A class to represent a dog, inheriting from Animal.
    Cat: A class to represent a cat, inheriting from Animal.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for animals.

    Methods:
        sound: Abstract method to be implemented by subclasses to make a sound.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method for making a sound.
        This method must be implemented by subclasses.

        Raises:
            NotImplementedError: If the method is not
            implemented by a subclass.
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal.

    Methods:
        sound: Returns the sound a dog makes.
    """

    def sound(self):
        """
        Return the sound a dog makes.

        Returns:
            str: The sound a dog makes ("Bark").
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal.

    Methods:
        sound: Returns the sound a cat makes.
    """

    def sound(self):
        """
        Return the sound a cat makes.

        Returns:
            str: The sound a cat makes ("Meow").
        """
        return "Meow"

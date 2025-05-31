"""
This module defines classes for Fish, Bird, and FlyingFish to
demonstrate multiple inheritance.

Classes:
    Fish: A class to represent a fish.
    Bird: A class to represent a bird.
    FlyingFish: A class to represent a flying fish, inheriting
    from both Fish and Bird.
"""


class Fish:
    """
    A class to represent a fish.

    Methods:
        swim: Prints a message indicating that the fish is swimming.
        habitat: Prints a message indicating the habitat of the fish.
    """

    def swim(self):
        """
        Print a message indicating that the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print a message indicating the habitat of the fish.
        """
        print("The fish lives in water")


class Bird:
    """
    A class to represent a bird.

    Methods:
        fly: Prints a message indicating that the bird is flying.
        habitat: Prints a message indicating the habitat of the bird.
    """

    def fly(self):
        """
        Print a message indicating that the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print a message indicating the habitat of the bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class to represent a flying fish, inheriting from both Fish and Bird.

    Methods:
        swim: Prints a message indicating that the flying fish is swimming.
        fly: Prints a message indicating that the flying fish is soaring.
        habitat: Prints a message indicating the habitat of the flying fish.
    """

    def swim(self):
        """
        Print a message indicating that the flying fish is swimming.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Print a message indicating that the flying fish is soaring.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Print a message indicating the habitat of the flying fish.
        """
        print("The flying fish lives both in water and the sky!")

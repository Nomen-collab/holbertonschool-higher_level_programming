#!/usr/bin/env python3
"""
This module defines an abstract base class `Shape` and its
subclasses `Circle` and `Rectangle`.

Classes:
    Shape: An abstract base class for shapes.
    Circle: A class to represent a circle, inheriting from Shape.
    Rectangle: A class to represent a rectangle, inheriting from Shape.

Functions:
    shape_info: Prints the area and perimeter of a shape.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for shapes.

    Methods:
        area: Abstract method to calculate the area of the shape.
        perimeter: Abstract method to calculate the perimeter of the shape.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle class that inherits from Shape.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius=0):
        """
        Initialize a new Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape.

    Args:
        shape (Shape): The shape object.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

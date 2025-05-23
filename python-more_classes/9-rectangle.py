#!/usr/bin/python3
"""
This module defines a class Rectangle that represents a rectangle.

The Rectangle class includes:
- Private instance attributes `__width` and `__height` to store
the dimensions of the rectangle.
- A public class attribute `number_of_instances` to keep track of
the number of Rectangle instances.
- A public class attribute `print_symbol` to store the symbol
used for string representation.
- A constructor to initialize the width and height with validation.
- Properties to retrieve the width and height.
- Property setters to set the width and height with validation.
- A method to calculate the area of the rectangle.
- A method to calculate the perimeter of the rectangle.
- A method to return a string representation of the rectangle using
the character(s) stored in `print_symbol`.
- A method to return a string representation of the rectangle to be
able to recreate a new instance by using `eval()`.
- A method to print the message 'Bye rectangle...' when an instance
of Rectangle is deleted.
- A static method to return the biggest rectangle based on the area.
- A class method to return a new Rectangle instance with
width == height == size.
"""


class Rectangle:
    """
    This class represents a rectangle with private width and height attributes.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol: The symbol used for string representation.
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle with a given width and height.

        Args:
            width (int): The width of the rectangle. Must be an integer >= 0.
            height (int): The height of the rectangle. Must be an integer >= 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width  # Use the setter for validation
        self.height = height  # Use the setter for validation
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle with validation.

        Args:
            value (int): The width of the rectangle. Must be an integer >= 0.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle with validation.

        Args:
            value (int): The height of the rectangle. Must be an integer >= 0.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        If width or height is equal to 0, perimeter is equal to 0.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using the
        character(s) stored in print_symbol.

        If width or height is equal to 0, returns an empty string.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rows = []
        for _ in range(self.__height):
            rows.append(str(self.print_symbol) * self.__width)
        return "\n".join(rows)

    def __repr__(self):
        """
        Returns a string representation of the rectangle to be able
        to recreate a new instance by using eval().

        Returns:
            str: The string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints the message 'Bye rectangle...' when an instance of
        Rectangle is deleted and decrements the number of instances.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The rectangle with the bigger area, or rect_1
            if both have the same area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance with width == height == size.

        Args:
            size (int): The size of the square. Must be an integer >= 0.

        Returns:
            Rectangle: A new Rectangle instance with width == height == size.
        """
        return cls(size, size)

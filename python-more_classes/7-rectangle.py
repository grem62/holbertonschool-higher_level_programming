#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by:
(based on 1-rectanlge.py)
"""


class Rectangle:
    """defined rectangle by: (based on 0-rectangle.py)"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.height * self.width)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")
        rectangle = [str(self.print_symbol) * self.width for _ in range(self.height)]
        return '\n'.join(rectangle)

    def __repr__(self):
        repre = repr(Rectangle)
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

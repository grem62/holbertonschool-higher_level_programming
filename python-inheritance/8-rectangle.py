#!/usr/bin/python3
"""module contains a class rectangle that
inherits from BaseGeometry"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """classe rectangle from Base geometry"""

    def __init__(self, width, height):
        """
        add the constructeur
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

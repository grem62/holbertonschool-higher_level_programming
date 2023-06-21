#!/usr/bin/python3
"""contains the module 9-rectangle inherits"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """define a square"""

    def __init__(self, size):
        self.integer_validator("size", size)

        super().__init__(size, size)
        self.__size = size
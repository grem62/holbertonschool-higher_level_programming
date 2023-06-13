#!/usr/bin/python3
"""Define a class square."""


class Square:
    '''Represent square.'''
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(self, size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size

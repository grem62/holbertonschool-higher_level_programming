#!/usr/bin/python3
"""class rectangle"""


from models.base import Base


class Rectangle(Base):
    """
    give a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        define axe and the width, height
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            return self.__width

        @property
        def height(self):
            return self.__height

        @property
        def x(self):
            return self.__x

        @property
        def y(self):
            return self.__y

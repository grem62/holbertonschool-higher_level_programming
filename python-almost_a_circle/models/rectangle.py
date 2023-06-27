#!/usr/bin/python3
"""class rectangle"""


from models.base import Base


class Rectangle(Base):
    """
    give a rectangle
    """

    signe_rectangle = '#'

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        define axe and the width, height
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    def area(self):
        """define a area for the rectangle"""
        return (self.height * self.width)

    def display(self):
        "display for the rectangle"
        height = self.height
        width = self.width
        x = self.x
        y = self.y

        for i in range(y):
            print()
        for j in range(height):
            print(" " * self.x + "#" * width)

    def __str__(self):
        """return string"""
        return (f"[Rectangle] ({self.id}) "f'{self.x}/{self.y} - '
                f'{self.width}/{self.height}')

    def update(self, *args):
        """ Update rectangle attributes. """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

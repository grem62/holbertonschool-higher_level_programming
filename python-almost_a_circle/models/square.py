#!/usr/bin/python3
"""
new classe the sqaure
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    create a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
    constructor of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the class Square
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'size' in kwargs:
            self.size = kwargs['size']
        if 'x' in kwargs:
            self.x = kwargs['x']
        if 'y' in kwargs:
            self.y = kwargs['y']

    def to_dictionary(self):
        """
        return a dictionary
        """
        return {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'width': self.width,
                'height': self.height
                }

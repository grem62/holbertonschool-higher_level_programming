#!/usr/bin/python3
"""
module 0-add_int
"""


def add_integer(a, b=98):
    """
    add integer
    addition two integer
    renvoie Value
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    return (a + b)

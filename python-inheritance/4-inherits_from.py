#!/usr/bin/python3
"""fonction determine if is a instance of calss"""


def inherits_from(obj, a_class):
    """
    Function to determine if obj is an instance of a_class
    inherited from the specified class.

    Args:
        obj: object to look at
        a_class: class to verify the instance of
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False

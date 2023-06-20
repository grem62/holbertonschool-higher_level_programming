#!/usr/bin/pythin3
"""
Finds if an object is an instance of a class.
"""


def is_kind_of_class(obj, a_class):
    """Function to determine if obj is an instance of a_class or
    class inherited.

    Args:
        obj: object to look at
        a_class: class to verify the instance of

    Returns: True if obj is an instance of a_class or inherited class,
             False otherwise
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False

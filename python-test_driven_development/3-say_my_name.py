#!/usr/bin/python3
"""
module 3 - say my name
"""


def say_my_name(first_name, last_name=""):
    """say_my_name

    Args:
        first_name: first name
        last_name: last_name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))

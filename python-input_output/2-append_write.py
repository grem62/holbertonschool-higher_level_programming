#!/usr/bin/python3
"""
Write a function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    returns the number of characters added:
    """

    with open(filename, "a", encoding="utf8") as file:
        new_file = file.write(text)
        return new_file

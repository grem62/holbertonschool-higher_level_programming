#!/usr/bin/python3
"""
open a file and read the text
"""


def write_file(filename="", text=""):

    """
    use the fonction open for be inside a file and after execute the setting
    """

    with open(filename, "w", encoding='utf-8') as fichier:
        file = fichier.write
        return len(text)

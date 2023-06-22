#!/usr/bin/python3
"""
open a file and read the text
"""


def read_file(filename=""):
    """
    use the fonction open for be inside a file and after execute the setting
    """

    with open(filename, "r", encoding='utf-8') as fichier:
        file = fichier.read()
        print(file, end="")

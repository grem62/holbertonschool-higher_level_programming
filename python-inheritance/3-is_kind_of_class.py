#!/usr/bin/python3
"""
Définition de la fonction is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Vérifie si obj est une instance de a_class en utilisant isinstance
    Retourne True si obj est une instance de a_class, sinon False
    """
    return True if isinstance(obj, a_class) else False

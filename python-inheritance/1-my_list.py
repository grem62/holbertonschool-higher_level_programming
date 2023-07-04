#!/usr/bin/python3
"""Définition de la classe MyList qui hérite de la classe list"""


class MyList(list):
    """
Définition de la méthode print_sorted
    """
    def print_sorted(self):
        """Utilisation de la fonction sorted pour trier la liste self"""
        print(sorted(self))

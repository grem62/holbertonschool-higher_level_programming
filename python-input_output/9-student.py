#!/usr/bin/python3
"""
class student
"""


class Student:
    """attribut of the class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        return a dictionarry of class student
        """

        return (getattr(self, "__dict__"))

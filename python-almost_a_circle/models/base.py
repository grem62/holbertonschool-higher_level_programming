#!/usr/bin/python3
"""class base"""


import json


class Base:
    """
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        json string
        """
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): is a list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or []:
            return []
        else:
            return json.loads(json_string)

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
        """

        """
        if list_objs is None:
            return []
        else:
            file_json = (cls.__name__ + '.json')
            json_string = \
                cls.to_json_string([b.to_dictionary() for b in list_objs])
            with open(file_json, 'w') as f:
                f.write(json_string)

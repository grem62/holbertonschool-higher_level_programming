#!/usr/bin/python3
"""
Write a function that returns the JSON representation of an object (string):
"""


import json


def to_json_string(my_obj):

    """
    json representation
    """

    json_representation = json.dumps(my_obj)
    return json_representation

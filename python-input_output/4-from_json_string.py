#!/usr/bin/python3
"""
Write a function that returns an object represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    args: my_str
    """
    json_representation = json.loads(my_str)
    return json_representation

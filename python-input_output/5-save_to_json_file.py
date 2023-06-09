#!/usr/bin/python3
"""
Write a function that writes an Object to a text file, using a JSON:
"""
import json


def save_to_json_file(my_obj, filename):
    """
    args: m_obj, filename
    """

    with open(filename, 'w') as f:
        return json.dump(my_obj, f)

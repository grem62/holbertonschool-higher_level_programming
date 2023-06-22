#!/usr/bin/python3
"""
Write a function that creates an Object from a “JSON file”:
"""
import json


def load_from_json_file(filename):
    """
    create object
    """
    with open(filename, 'r') as f:
        json_file = f.read()
        objet = json.loads(json_file)
        return objet

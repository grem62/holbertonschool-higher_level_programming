#!/usr/bin/python3


def class_to_json(obj):
    """
    get attribu of a dictionnaire for json serialization
    """

    return getattr(obj, '__dict__')

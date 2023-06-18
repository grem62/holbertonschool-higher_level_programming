#!/usr/bin/python3


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiteur = ['.', '?', ':']
    for char in text:
        print(char, end='')
        if char in delimiteur:
            print('\n' * 2, end='')

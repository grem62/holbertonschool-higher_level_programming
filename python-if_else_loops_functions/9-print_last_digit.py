#!/usr/bin/python3
def print_last_digit(number):

    index = abs(number) % 10
    print(index, end='')
    return index

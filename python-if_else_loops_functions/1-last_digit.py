#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10

print("Last digit of", number, "is", lastdigit, end=' ')

if number < 6:
    print("and is less than 6 and not 0")
if number == 0:
    print("and is zero")
if number > 5:
    print("and is greater than 5")

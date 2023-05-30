#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
print("Last digit of", number, "is", lastdigit, end=' ')
if number > 5:
    print(f"and is greater than 5")
if number < 6:
    print(f"and is less than 6 and not 0")
if number == 0:
    print(f"and is 0")

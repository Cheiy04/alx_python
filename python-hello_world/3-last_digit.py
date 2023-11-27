#!/usr/bin/python3
import random
number = str(random.randint(-10000, 10000))
last_digit =int(number[-1])

if last_digit > 5:
    print("Last digit of", 98, "is", 8, "and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print("Last digit of", -98, "is", -8, "and is less than 6 and not 0")
else: 
    print("Last digit of", 0, "is", 0, "and is 0")


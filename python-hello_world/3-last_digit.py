import random

# Generate a random number between -10000 and 10000 (inclusive)
number = random.randint(-10000, 10000)


if number >= 0:
    last_digit = number % 10
else:
    last_digit = -(-number % 10)
    
#  an empty string to hold the classification
classification = ""

if last_digit > 5:
    classification = "and is greater than 5"

if last_digit == 0:
    classification = "and is 0"

if last_digit < 6 and last_digit != 0:
    classification = "and is less than 6 and not 0"

# Print the result
print("Last digit of {} is {} {}".format(number, last_digit, classification))

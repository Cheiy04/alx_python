# functions that takes temp in fahrenheit and returns in degrees
def convert_to_celsius(a):
    degrees = (a-32) * (5/9)
    degrees = round(degrees, 13)
    return degrees

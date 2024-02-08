'''Creating the class BaseGeometry'''
class BaseGeometry:
    '''Creating a method to raise an exception'''
    def area(self):
        raise Exception('area() is not implemented')
    '''Checks if the value is an positive integer'''
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

'''Creating the class rectangle that inherits from BaseGeometry'''
class Rectangle(BaseGeometry):
    '''Initializing...'''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    '''Method that prints the result'''
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    '''Method that calculates the area'''
    def area(self):
        return self.__width * self.__height
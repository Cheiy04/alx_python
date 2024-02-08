'''creating the class BaseGeometry'''
class BaseGeometry:
    '''Method that checks for exception'''
    def area(self):
        raise Exception('area() is not implemented')
    
    '''Method that checks if the value is a positive integer'''
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

'''Creating class rectangle that inherits from BaseGeometry'''
class Rectangle(BaseGeometry):
    '''Constructor that initializes our values'''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    '''Method that prints the output'''
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    '''Method that calculates our area'''
    def area(self):
        return self.__width * self.__height


'''Creating a class Square that inherits from Rectangle'''
class Square(Rectangle):
    '''Constructor that initializes our values'''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    '''Method that prints the output'''
    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
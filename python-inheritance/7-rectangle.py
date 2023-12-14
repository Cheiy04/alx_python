'''Importing the previous file'''
BaseGeometry = __import__('5-base_geometry').BaseGeometry

'''Creating a new class that inherits form the BaseGeometry'''

class Rectangle(BaseGeometry):

    '''Initializing our proparties and also initializing the inherited class'''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
    '''Function that calculates the area of the rectangle'''
    def area(self):
        '''Return the area of the rectangle:  width by the height'''
        return self.__width * self.__height

    '''String representaion of our rectangle'''
    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
    

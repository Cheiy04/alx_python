'''Importing the base file'''
from models.base import Base

'''Creating the class rectangle that inherits from Base'''
class Rectangle(Base):
    '''Creating instance attributes to contain width and height
        Calling the super() function from the Base class
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    '''Creating getters and setters for all the created instance'''
    @property
    def width(self):
        '''Retrives the width of the rectangle'''
        return self.__width
    
    @width.setter
    def width(self, value):
        '''setter for the widht of the rectangle'''
        '''Raising exceptions if the input is not an integer or input is <= 0'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(value))
        if value <= 0:
            raise ValueError("{} must be > 0".format(value))
        
        self.__width = value


    '''Getter and setter for the height'''
    @property
    def height(self):
        '''Retrives the height of the rectangle'''
        return self.__height
    
    @height.setter
    def height(self, value):
        '''setter for the height of the rectangle'''

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(value))
        if value <= 0:
            raise ValueError("{} must be > 0".format(value))
        self.__height = value

    '''Getter and setter for the x value'''
    @property
    def x(self):
        '''Retrives the x value'''
        return self.__x
    
    @x.setter
    def x(self, value):
        '''setter for the x value'''

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(value))
        if value < 0:
            raise ValueError("{} must be >= 0".format(value))
        self.__x = value

    '''Getter and setter for y value'''
    @property
    def y(self):
        '''Retrives the y value'''
        return self.__y
    
    @y.setter
    def y(self, value):
        '''setter for the y value'''

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(value))
        if value < 0:
            raise ValueError("{} must be >= 0".format(value))
        self.__y = value

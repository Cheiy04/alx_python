'''Importing the base file'''
from base import Base

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

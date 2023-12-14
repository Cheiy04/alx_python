'''Class base geometry '''
class BaseGeometry:
    '''Method that raises an exceptions if not implemented'''
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        '''If value is not an integer raise a Type error'''
        if not isinstance(value, int):
            raise TypeError('name must be an integer')

        '''If value is less than or equall to zero'''
        if value <= 0:
            raise ValueError('name must be greater than 0')
        
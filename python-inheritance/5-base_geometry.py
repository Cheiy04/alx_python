'''Class base geometry '''
class BaseGeometry:
    '''Method that raises an exceptions if not implemented'''
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        '''If value is not an integer raise a Type error'''
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))

        '''If value is less than or equall to zero'''
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
        
    def __dir__(self):
        """
        Customize the dir() output to specify the order of attributes.

        Returns:
            list: A sorted list of attribute names.
        """
        return sorted(['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
                       '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
                       '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
                       '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
                       'area', 'integer_validator'])
        
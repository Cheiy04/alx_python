'''Class base geometry '''
class BaseGeometry:
    '''Method that raises an exceptions if not implemented'''
    def area(self):
        raise Exception("area() is not implemented")
        
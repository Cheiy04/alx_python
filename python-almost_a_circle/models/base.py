class Base:
    '''Class that defines the properties of Base'''
    '''Creating a static attribute'''
    __nb_objects = 0

    '''Creating new instances of our base'''
    def __init__(self, id =None):
        '''Check if the instance id is not set to none'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects



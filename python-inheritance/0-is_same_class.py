'''Define a function is_same_class'''

def is_same_class(obj, a_class):
    '''Check whether the object is instance of class
        returns True if it is 
        return False if its not
    '''
    return type(obj) == a_class
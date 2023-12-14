'''Function inherits_from'''

def inherits_from(obj, a_class):
    '''Function that cheks if the object is instance of class it inhertited from(Directly or inderictly)'''
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)


'''Importing rectangle class to the square class'''
from models.rectangle import Rectangle

'''Creating class square'''
class Square(Rectangle):
    '''Class square that has inherited all logic from rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Creating new instances for the square and calling the instances from rectangle'''
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.size)
    
if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()
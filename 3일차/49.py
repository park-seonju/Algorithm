class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length**2
a=Square(3)
print('정사각형의 면적: {}'.format(a.area()))
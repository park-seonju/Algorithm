class Rectangle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def cal(self):
        return self.x*self.y
a=Rectangle(2,10)
print('사각형의 면적:',a.cal())
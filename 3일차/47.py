class Circle:
    def __init__(self,radius):
        self.radius=radius
    def cal(self):
        return '원의 면적: {}'.format(2*3.14*self.radius)
a=Circle(2)
print(a.cal())
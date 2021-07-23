class Student:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return '이름: {}'.format(self.name)
class GraduateStudent(Student):
    def __init__(self,name,major):
        super().__init__(name)
        self.major=major
    def __repr__(self):
        return super().__repr__() + ', 전공: {}'.format(self.major)

a=Student('홍길동')
b=GraduateStudent('이순신','컴퓨터')
print(a)
print(b)
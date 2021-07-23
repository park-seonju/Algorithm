class Student:
    def __init__(self, kor, math, eng):
        self.kor = kor
        self.math = math
        self.eng = eng

    def kor(self):
        return self.kor

    def math(self):
        return self.math

    def eng(self):
        return self.eng

    def get_total(self):
        return self.kor + self.math + self.eng
a = input()
a = a.split(", ")
a = list(map(int, a))
student = student(a[0], a[1], a[2])
print("국어, 영어, 수학의 총점: {}".format(student.get_total()))
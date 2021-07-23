# class Korean:
#     def __init__(self,Nation): #객체 만드는거임. 고로 정적메서드가 아님
#         self.Nation=Nation
#     def printNationality(self):
#         return self.Nation
# a='대한민국'
# a=Korean(a)
# print(a.printNationality())
# print(a.printNationality())


class Korean:
    def printNationality():
        return '대한민국'

print(Korean.printNationality())
print(Korean.printNationality())
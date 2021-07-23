class Person:
    def getGender(self):
        return 'Unknown'
class Male(Person):
    def getGender(self):
        return "Male"
class Female(Person):
    def getGender(self):
        return "Female"
s1 = Male()
s2 = Female()
 
print(s1.getGender())
print(s2.getGender())
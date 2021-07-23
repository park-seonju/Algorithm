import datetime
name=input()
age = int(input())
year=datetime.datetime.now().year+100-age
print("{}(은)는 {}년에 100세가 될 것입니다.".format(name,year))
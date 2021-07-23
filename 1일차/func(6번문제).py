list1=[2,4,6,8,10]
print(list1)
def find(list1,n):
    if n in list1:
        print(n,'=> True')
    elif n not in list1:
        print(n,'=> False')
find(list1,5)
find(list1,10)
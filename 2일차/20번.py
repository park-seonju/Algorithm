a=list(map(int,input().split(', ')))
list1=[i for i in a if i%2 != 0]
print(", ".join(map(str,list1)))
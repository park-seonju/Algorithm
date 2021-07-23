import sys

a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
c=int(sys.stdin.readline())
d=int(sys.stdin.readline())
e=int(sys.stdin.readline())
list1=[a,b,c,d,e]
print("입력된 값 {}의 평균은 {}입니다.".format(list1,sum(list1)/len(list1)))
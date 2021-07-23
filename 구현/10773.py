import sys
input=sys.stdin.readline
Test=int(input())
total=[]
while Test>0:
    Test-=1
    num=int(input())
    if num :
        total.append(num)    
    else:
        total.pop()
print(sum(total))
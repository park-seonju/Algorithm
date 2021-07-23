import sys
input=sys.stdin.readline
A,B=map(int,input().split())
num=int(input())
num_list=list(map(int,input().split()))
num_list.reverse()

decimal=0
for i in range(num):
    decimal+=(A**i)*num_list[i]

ans=[]

while decimal !=0:
    ans.append(decimal % B)
    decimal = decimal // B

print(*ans[::-1])
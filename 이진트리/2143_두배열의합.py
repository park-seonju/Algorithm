import sys
input=sys.stdin.readline
T=int(input())
n=int(input())
A=list(map(int,input().split()))
m=int(input())
B=list(map(int,input().split()))

temp={}

ans=0

for i in range(n):
    for j in range(i,n):
        temp[sum(A[i:j+1])]=temp.get(sum(A[i:j+1]),0)+1

for i in range(m):
    for j in range(i,m):
        if T-sum(B[i:j+1]) in temp:
            ans+=temp[T-sum(B[i:j+1])]
print(ans)
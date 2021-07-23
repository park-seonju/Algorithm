import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n,m=map(int,input().split())
parents=[i for i in range(n)]

def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

def union(x,y):
    r1=find(x)
    r2=find(y)
    if r1!=r2:
        parents[r2]=r1
        
for i in range(m):
    a,b=map(int,input().split())
    if find(a)==find(b):
        print(i+1)
        break
    union(a,b)
else:
    print(0)
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

def union(x,y):
    root1=find(x)
    root2=find(y)
    parents[root2]=root1

n=int(input())
m=int(input())
parents=[i for i in range(n+1)]

# 0 1 0 
# 1 0 1
# 0 1 0
for i in range(n):
    info=list(map(int,input().split()))
    for j in range(i+1,n):
        if info[j]:
            union(i+1,j+1)
plan=list(map(int,input().split()))
root=find(plan[0])
flag=False
for i in range(m):
    if find(plan[i])!=root:
        flag=True
        break
if flag:print('NO')
else:print('YES')
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

n,m=map(int,input().split())
info=[list(map(int,input().split())) for _ in range(m)]
parents=[x for x in range(n+1)]

for i in info:
    if not i[0]:
        union(i[1],i[2])
    if i[0]:
        if find(i[1]) == find(i[2]):
            print('YES')
        else:
            print('NO')
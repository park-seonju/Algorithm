import math

n=int(input())
info=[list(map(float,input().split())) for _ in range(n)]
dist=[]
parents=[i for i in range(n)]
ranks=[0 for i in range(n)]

def find(x):
    if parents[x] != x:
        parents[x]=find(parents[x])
    return parents[x]

def union(x,y):
    root1=find(x)
    root2=find(y)
    parents[root2]=root1

def kruskal(n):
    mst_cost=0
    for val,s,e in dist:
        if find(s) != find(e):
            mst_cost += val
            union(s,e)
    print(mst_cost)


for i in range(n):
    for j in range(i+1,n):
        distance=math.sqrt((info[i][0]-info[j][0])**2 + (info[i][1]-info[j][1])**2)
        dist.append((distance,i,j))
        dist.append((distance,j,i))
dist.sort()
kruskal(n)
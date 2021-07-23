import math

n,m=map(int,input().split())
info=[list(map(int,input().split())) for _ in range(n)]
dist=[]
parents=[i for i in range(n+1)]


def find(x):
    if parents[x] != x:
        parents[x]=find(parents[x])
    return parents[x]

def union(x,y):
    root1=find(x)
    root2=find(y)
    parents[root2]=root1

def kruskal(n):
    global M_cnt
    ans=0
    for val,s,e in dist:
        if find(s) != find(e):
            ans += val
            union(s,e)
            M_cnt+=1
        if M_cnt == n-1:break
    print("{:.2f}".format(ans))

M_cnt=0
for _ in range(m):
    a,b=map(int,input().split())
    if find(a-1)!=find(b-1):
        union(a-1,b-1)
        M_cnt+=1

for i in range(n-1):
    for j in range(i+1,n):
        distance=math.sqrt((info[i][0]-info[j][0])**2 + (info[i][1]-info[j][1])**2)
        dist.append((distance,i,j))
dist.sort()
kruskal(n)
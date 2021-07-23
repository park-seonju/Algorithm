import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
T=int(input())
def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

def union(x,y):
    root1=find(x)
    root2=find(y)
    if root1 != root2:
        parents[root2]=root1
        num[root1]+=num[root2]

for tc in range(T):
    F=int(input())
    parents={}
    num={}
    for _ in range(F):
        p1,p2=map(str,input().split())
        if p1 not in parents:
            parents[p1]=p1
            num[p1]=1
        if p2 not in parents:
            parents[p2]=p2
            num[p2]=1
        union(p1,p2)
        print(num[find(p1)])
import sys
input= sys.stdin.readline
sys.setrecursionlimit(60000)
n=int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    n1,n2,d=map(int,input().split())
    adj[n1].append([n2,d])
    adj[n2].append([n1,d])

parents=[0]*(n+1)
visited=[False]*(n+1)
dists=[0]*(n+1)
d=[0]*(n+1)
def dfs(node,distance,depth):
    visited[node]=True
    d[node]=depth
    for e,dist in adj[node]:
        if not visited[e]:
            dists[e]=distance+dist
            parents[e]=node
            dfs(e,distance+dist,depth+1)

dfs(1,0,0)

def LCA(a,b):
    while d[a]!=d[b]:
        if d[a]>d[b]:
            a=parents[a]
        elif d[a]<d[b]:
            b=parents[b]
    while a!=b:
        a=parents[a]
        b=parents[b]
    return a
m=int(input())
ans=[]
for _ in range(m):
    f1,f2=map(int,input().split())
    common_parent_node=LCA(f1,f2)
    ans.append(dists[f1]+dists[f2]-(2*dists[common_parent_node]))
print('\n'.join(*ans))
    
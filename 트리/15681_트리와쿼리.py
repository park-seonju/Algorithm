import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
def countSubtreeNodes(current):
    size[current]=1
    for e in adj[current]:
        if not size[e]:
            countSubtreeNodes(e)
            size[current]+=size[e]
            
n,r,q=map(int,input().split())
adj=[[] for _ in range(n+1)]
size=[0]*(n+1)

for _ in range(n-1):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

countSubtreeNodes(r)

for _ in range(q):
    Q=int(input())
    print(size[Q])
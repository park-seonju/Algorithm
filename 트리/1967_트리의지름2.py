import sys
sys.setrecursionlimit(10**6)
def dfs(s,dist):
    for node,e in adj[s]:
        if not dist[node]:
            dist[node]=dist[s]+e
            dfs(node,dist)

n=int(input())
adj=[[] for _ in range(n+1)]
for _ in range(n-1):
    parent,child,e=map(int,input().split())
    adj[parent].append((child,e))
    adj[child].append((parent,e))

first_result=[0]*(n+1)
dfs(1,first_result)
first_result[1]=0

maximum=max(first_result)
maxnode=first_result.index(maximum)


result=[0 for _ in range(n+1)]
dfs(maxnode,result)
result[maxnode]=0
print(max(result))
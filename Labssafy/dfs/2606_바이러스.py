def dfs(idx):
    global cnt
    cnt+=1
    visited[idx]=True
    for e in adj[idx]:
        if not visited[e]:
            dfs(e)
n=int(input())
v=int(input())
adj=[[] for _ in range(n+1)]
visited=[False]*(n+1)
cnt=0
for _ in range(v):
    s,e=map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)
dfs(1)
print(cnt-1)

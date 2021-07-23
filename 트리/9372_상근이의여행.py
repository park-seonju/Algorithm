import sys
input=sys.stdin.readline
def dfs(n,cnt):
    visited[n]=1
    for i in adj[n]:
        if not visited[i]:
            cnt = dfs(i,cnt+1)
    return cnt
    
T=int(input())
for tc in range(T):
    n,m=map(int,input().split())
    adj= [[] for _ in range(n+1)]
    visited=[0 for _ in range(n+1)]
    for _ in range(m):
        s,e=map(int,input().split())
        adj[s].append(e)
        adj[e].append(s)
    cnt = dfs(1,0)
    print(cnt)
    # print(n-1)
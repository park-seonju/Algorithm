from collections import deque

N=int(input())
p1,p2=map(int,input().split())
M=int(input())
adj = [[] for _ in range(N+1)]
visited = [False] * (N+1)

def bfs(v,target):
    cnt=0
    q=deque([[v,cnt]])
    while q:
        value=q.popleft()
        v=value[0]
        cnt=value[1]
        if v==target:
            return cnt
        if not visited[v]:
            visited[v]=True
            cnt+=1
            for e in adj[v]:
                if not visited[e]:
                    q.append([e,cnt])
    return -1

for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

print(bfs(p1,p2))

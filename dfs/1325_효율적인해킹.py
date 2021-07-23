from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
adj= [[] for _ in range(n+1)]
for _ in range(m):
    c1,c2=map(int,input().split())
    adj[c2].append(c1)

answer=[0]
for i in range(1,n+1):
    visited=[0]*(n+1)
    visited[i]=1
    if adj[i]:
        q=deque()
        q.append(i)
        while q:
            node=q.popleft()
            for e in adj[node]:
                if not visited[e]:
                    visited[e]=1
                    q.append(e)
    answer.append(visited.count(1))
cnt=max(answer)
real=[]
for i in range(1,n+1):
    if answer[i]==cnt:
        real.append(i)
print(*real)
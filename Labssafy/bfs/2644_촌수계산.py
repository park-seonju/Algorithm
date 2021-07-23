from collections import deque
n=int(input())
p1,p2=map(int,input().split())
m=int(input())
adj=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for _ in range(m):
    x,y=map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)
q=deque([(p1,0)])
visited[p1]=1
while q:
    node,cnt=q.popleft()
    if node==p2:break
    for e in adj[node]:
        if not visited[e]:
            visited[e]=1
            q.append((e,cnt+1))
if visited[p2]:print(cnt)
else:print(-1)
            

import sys
from collections import deque
input=sys.stdin.readline
F,S,G,U,D=map(int,input().split())
visited=[0]*(F+1)

q=deque()
q.append((S,0))
visited[S]=1
while q:
    start,cnt=q.popleft()
    if start==G:print(cnt);exit()
    
    if start+U<=F and not visited[start+U]:
        visited[start+U]=1
        q.append((start+U,cnt+1))
    
    if start-D>=1 and not visited[start-D]:
        visited[start-D]=1
        q.append((start-D,cnt+1))

print('use the stairs')
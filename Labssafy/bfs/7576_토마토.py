from collections import deque
import sys
input=sys.stdin.readline
m,n=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
dx=[0,0,-1,1]
dy=[-1,1,0,0]
q=deque()
for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            q.append((i,j,0))

ans=0
while q:
    x,y,cnt=q.popleft()
    if ans<cnt: ans=cnt
    for _ in range(4):
        nx=dx[_]+x
        ny=dy[_]+y
        if 0<=nx<n and 0<=ny<m:
            if board[nx][ny]==0 and not visited[nx][ny]:
                visited[nx][ny]=1
                board[nx][ny]=1
                q.append((nx,ny,cnt+1))
for i in range(n):
    for j in range(m):
        if board[i][j]==0:
            print(-1)
            exit()
print(ans)
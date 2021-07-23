import sys
from collections import deque
input=sys.stdin.readline
m,n,h=map(int,input().split())
board=[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
visited=[[[0]*m for _ in range(n)] for _ in range(h)]
dx=[0,0,-1,1,0,0]
dy=[-1,1,0,0,0,0]
dz=[0,0,0,0,-1,1]
q=deque()
flag=True

for z in range(h):
    for i in range(n):
        for j in range(m):
            if board[z][i][j]==1:
                q.append((z,i,j,0))
            elif board[z][i][j]==0:
                flag=False
if flag:print(0);exit()
ans=0
while q:
    z,x,y,cnt=q.popleft()
    for _ in range(6):
        nx=x+dx[_]
        ny=y+dy[_]
        nz=z+dz[_]
        if 0<=nx<n and 0<=ny<m and 0<=nz<h:
            if board[nz][nx][ny]==0 and not visited[nz][nx][ny]:
                visited[nz][nx][ny]=1
                board[nz][nx][ny]=1
                ans=cnt+1
                q.append((nz,nx,ny,cnt+1))

for z in range(h):
    for i in range(n):
        for j in range(m):
            if board[z][i][j]==0:
                print(-1)
                exit()
print(ans)

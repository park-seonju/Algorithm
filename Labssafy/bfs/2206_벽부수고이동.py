import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
board=[input() for _ in range(n)]
dx=[0,0,-1,1]
dy=[-1,1,0,0]
visited = [[[0] * 2 for i in range(m)] for i in range(n)]

q=deque()
q.append((0,0,1))
visited[0][0][1]=1
ans=10000001
while q:
    i,j,bomb=q.popleft()
    if i==n-1 and j==m-1: ans=visited[i][j][bomb]
    for _ in range(4):
        nx=dx[_]+i
        ny=dy[_]+j
        if 0<=nx<n and 0<=ny<m:
                if board[nx][ny]=='1' and bomb==1: # 벽이고 뿌실수있다면
                    visited[nx][ny][0]=visited[i][j][1]+1  # 0:뿌신곳 거리 1:안뿌신곳에서+1한거
                    q.append((nx,ny,0)) # 다음에 넣어줄땐 뿌셨으니 0 넣어줌
                elif board[nx][ny]=='0' and not visited[nx][ny][bomb]:  # 그냥 갈수있고 방문안했으면
                    visited[nx][ny][bomb]=visited[i][j][bomb]+1 # 거길 뿌셨던 안뿌셨던 bomb에다가 +1 해줌
                    q.append((nx,ny,bomb))

if visited[n-1][m-1]:
    print(ans)
else:
    print(-1)
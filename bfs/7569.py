import sys
from collections import deque
input=sys.stdin.readline

m,n,h=map(int,input().split())
board=[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

# 0000
# 1110
# 0000
dx=[1,-1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,1,-1]

que=deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k]==1:
                que.append([i,j,k])
while que:
    z,x,y=que.popleft()
    for i in range(6):
        nx=x+dx[i]
        ny=y+dy[i]
        nz=z+dz[i]
        if 0 <=nx<n and 0 <=ny<m and 0 <=nz<h:
            if board[nz][nx][ny]==0:
                board[nz][nx][ny]=board[z][x][y]+1
                que.append([nz,nx,ny])

result=0
def ans(result):
    for i in board:
        for j in i:
            for k in j:
                if k==0:
                    result=-1
                    return result
                else:
                    result=max(result,k)
    return result-1  # 1부터 1을 더한것이므로 -1해줌

print(ans(result))

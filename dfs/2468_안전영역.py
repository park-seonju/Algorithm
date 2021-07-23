import copy
import sys
sys.setrecursionlimit(100000)
def dfs(i,j,temp):
    temp[i][j]=0 #탐색한곳
    for _ in range(4):
        ny=i+dy[_]
        nx=j+dx[_]
        if 0<=nx<N and 0<=ny<N:
            if temp[ny][nx] != 0:
                dfs(ny,nx,temp)

N=int(input())
board=[list(map(int,input().split())) for _ in range(N)]
high=0
ans=1
dx=[0,0,-1,1] #상하좌우
dy=[-1,1,0,0]

for i in range(N):
    for j in range(N):
        if high<board[i][j]:
            high=board[i][j]

for h in range(1,high):
    temp=copy.deepcopy(board)
    for i in range(N):
        for j in range(N):
            if board[i][j] <= h:
                temp[i][j]=0
    cnt = 0
    for y in range(N):
        for x in range(N):
            if temp[y][x]!=0:
                dfs(y,x,temp)
                cnt+=1
    ans=max(ans,cnt)
print(ans)
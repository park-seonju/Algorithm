from collections import deque
import sys
input=sys.stdin.readline
dx=[0,0,-1,1]
dy=[-1,1,0,0]
def group(i,j):
    q=deque([(i,j)])
    board[i][j]=grouping
    while q:
        x,y=q.popleft()
        for _ in range(4):
            nx=x+dx[_]
            ny=y+dy[_]
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny]==1:
                    board[nx][ny]=grouping
                    q.append((nx,ny))
                elif board[nx][ny]==0 and not (x,y) in wide:
                    wide.append((x,y))
def dist():
    loop=0
    ans=sys.maxsize
    while wide: # 전체 바다와 인접한 갯수만큼
        loop+=1
        length=len(wide) # 현재 바다와 인접한 갯수
        for _ in range(length): # 현재 바다와 인접한 갯수만큼 반복
            x,y=wide.popleft()
            for _ in range(4):
                nx=x+dx[_]
                ny=y+dy[_]
                if 0<=nx<n and 0<=ny<n:
                    if board[nx][ny]==0:
                        board[nx][ny]=board[x][y]
                        wide.append((nx,ny))
                    elif board[nx][ny]<board[x][y]:
                        ans=min(ans,(loop-1)*2)
                    elif board[nx][ny]>board[x][y]:
                        ans=min(ans,loop*2-1)
    return ans
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
grouping=-1
wide=deque() # 바다와 맞닿은곳
for i in range(n):
    for j in range(n):
        if board[i][j]>0:
            group(i,j)
            grouping-=1

print(dist())
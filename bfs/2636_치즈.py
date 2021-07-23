from collections import deque
n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
time=0
dx=[0,0,-1,1]
dy=[-1,1,0,0]
def melt(i,j):
    visited=[[0]*m for _ in range(n)]
    q=deque()
    q.append((i,j))
    visited[i][j]=1
    board[i][j]=2
    while q:
        x,y=q.popleft()
        for _ in range(4):
            nx=x+dx[_]
            ny=y+dy[_]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and (board[nx][ny]==0 or board[nx][ny]==2) :
                    visited[nx][ny]=1
                    board[nx][ny]=2
                    q.append((nx,ny))

def RemoveCheck(i,j):
    global cnt
    for _ in range(4):
        nx=i+dx[_]
        ny=j+dy[_]
        if board[nx][ny]==2:
            board[i][j]=0
            cnt+=1
            return
cnt=0
while 1:
    end=True

    for i in range(n):
        for j in range(m):
            if board[i][j]==1:
                end=False
                break
        if not end:
            break
    if end:
        print(time)
        print(cnt)
        exit()
    cnt=0
    melt(0,0)

    for i in range(n):
        for j in range(m):
            if board[i][j]==1:
                RemoveCheck(i,j)
    time+=1
dx=[0,0,-1,1]
dy=[-1,1,0,0]
from collections import deque
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
group=[[0]*n for _ in range(n)]
group_num=1
ans=999999999
def Grouping(i,j,group_num):
    q=deque()
    q.append((i,j))
    group[i][j]=group_num
    while q:
        x,y=q.popleft()
        for _ in range(4):
            nx=x+dx[_]
            ny=y+dy[_]
            if 0<=nx<n and 0<=ny<n:
                if group[nx][ny]==0 and board[nx][ny]==1:
                    q.append((nx,ny))
                    group[nx][ny]=group_num

def bfs(num):
    global ans
    dist=[[-1]*n for _ in range(n)]
    q=deque()
    for i in range(n):
        for j in range(n):
            if group[i][j]==num:
                q.append((i,j))
                dist[i][j]=0
    while q:
        x,y=q.popleft()
        for _ in range(4):
            nx=x+dx[_]
            ny=y+dy[_]
            if 0<=nx<n and 0<=ny<n:
                if group[nx][ny]!=0 and group[nx][ny]!=num:
                    ans=min(ans,dist[x][y])
                    return
                if group[nx][ny]==0 and dist[nx][ny]==-1:
                    dist[nx][ny]=dist[x][y]+1
                    q.append((nx,ny))

for i in range(n):
    for j in range(n):
        if not group[i][j] and board[i][j]==1:
            Grouping(i,j,group_num)
            group_num+=1

for num in range(1,group_num):
    bfs(num)

print(ans)
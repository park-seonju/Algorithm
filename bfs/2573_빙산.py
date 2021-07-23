from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
visited=[[False]*m for _ in range(n)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]
year=0
cnt=0

def bfs(i,j):
    q=deque()
    q.append((i,j))
    visited[i][j]=True
    while q:
        x,y=q.popleft()
        for _ in range(4):
            nx=x+dy[_]
            ny=y+dx[_]
            if board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny]=True
                q.append((nx,ny))

for i in range(1,n-1):  # 예외)처음에 떨어져있는 경우 확인
        for j in range(1,m-1):
            if board[i][j] and not visited[i][j]:
                cnt+=1 #빙산 갯수
                bfs(i,j)
if cnt>=2:
    print(year)
    exit()
while cnt == 1:
    decrease=[[0]*m for _ in range(n)] # 빼줄 숫자 보드선언
    visited=[[False]*m for _ in range(n)]
    for i in range(1,n-1):
        for j in range(1,m-1):
            if board[i][j] != 0: #빙산있으면
                for _ in range(4): # 4방향탐색
                    nx=i+dy[_]
                    ny=j+dx[_]
                    if board[nx][ny]==0:
                        decrease[i][j]+=1
                        
    for i in range(1,n-1):
        for j in range(1,m-1):
            if board[i][j]-decrease[i][j] < 0:
                board[i][j]=0
            else:
                board[i][j]-=decrease[i][j]
    year+=1
    cnt=0
    for i in range(1,n-1):
        for j in range(1,m-1):
            if board[i][j] and not visited[i][j]:
                cnt+=1
                bfs(i,j)
if cnt>=2:
    print(year)
else: # cnt 0일때
    print(0)

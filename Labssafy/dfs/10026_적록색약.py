import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def normal(i,j):
    visited[i][j]=1
    for _ in range(4):
        nx=i+dx[_]
        ny=j+dy[_]
        if 0<=nx<n and 0<=ny<n:
            if board[i][j]==board[nx][ny] and not visited[nx][ny]:
                normal(nx,ny)

def diff(i,j):
    visited[i][j]=1
    for _ in range(4):
        nx=i+dx[_]
        ny=j+dy[_]
        if 0<=nx<n and 0<=ny<n:
            if (board[nx][ny]=='R' or board[nx][ny]=='G') and not visited[nx][ny]:
                diff(nx,ny)

n=int(input())
board=[input().rstrip() for _ in range(n)]
visited=[[0]*n for _ in range(n)]
dx=[0,0,-1,1]
dy=[-1,1,0,0]
no=0
yes=0
for i in range(n):
    for j in range(n):
        if board[i][j]=='R' and not visited[i][j]:
            no+=1
            normal(i,j)
        elif board[i][j]=='G' and not visited[i][j]:
            no+=1
            normal(i,j)
        elif board[i][j]=='B' and not visited[i][j]:
            no+=1
            normal(i,j)
visited=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (board[i][j]=='R' or board[i][j]=='G') and not visited[i][j]:
            yes+=1
            diff(i,j)
        elif board[i][j]=='B' and not visited[i][j]:
            yes+=1
            normal(i,j)
print(no,yes)
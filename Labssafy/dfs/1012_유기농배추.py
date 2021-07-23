import sys
sys.setrecursionlimit(10**6)

dx=[0,0,-1,1]
dy=[-1,1,0,0]
def dfs(i,j):
    visited[i][j]=1
    for _ in range(4):
        nx=i+dx[_]
        ny=j+dy[_]
        if 0<=nx<n and 0<=ny<m:
            if board[nx][ny]==1 and not visited[nx][ny]:
                dfs(nx,ny)
T=int(input())
for _ in range(T):
    m,n,k=map(int,input().split())
    board=[[0]*m for _ in range(n)]
    visited=[[0]*m for _ in range(n)]
    for _ in range(k):
        x,y=map(int,input().split())
        board[y][x]=1
    cnt=0
    for i in range(n):
        for j in range(m):
            if board[i][j] and not visited[i][j]:
                cnt+=1
                dfs(i,j)
    print(cnt)

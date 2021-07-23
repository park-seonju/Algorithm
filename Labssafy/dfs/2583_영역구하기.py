import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def dfs(i,j):
    global cnt
    cnt+=1
    visited[i][j]=1
    for _ in range(4):
        nx=i+dx[_]
        ny=j+dy[_]
        if 0<=nx<n and 0<=ny<m and not board[nx][ny] and not visited[nx][ny]:
            visited[nx][ny]=1
            dfs(nx,ny)

m,n,k=map(int,input().split())
board=[[False]*m for _ in range(n)]
visited=[[0]*m for _ in range(n)]
for _ in range(k):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(min(x1,x2),max(x1,x2)):
        for j in range(min(y1,y2),max(y1,y2)):
            board[i][j]=True
ans=[]
local=0
for i in range(n):
    for j in range(m):
        cnt=0
        if not board[i][j] and not visited[i][j]:
            local+=1
            dfs(i,j)
            ans.append(cnt)
ans.sort()
print(local)
print(*ans)
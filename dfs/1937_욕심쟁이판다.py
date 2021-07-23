import sys
sys.setrecursionlimit(1000000)
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
ans=1
dx=[0,0,-1,1]
dy=[-1,1,0,0]
visited=[[0 for _ in range(n)] for __ in range(n)]
def dfs(i,j):
    if not visited[i][j]:
        for _ in range(4):
            nx = i+dx[_]
            ny = j+dy[_]
            if 0<=nx<n and 0<=ny<n:
                if board[i][j]<board[nx][ny]:
                    visited[i][j]=max(visited[i][j],dfs(nx,ny))
        visited[i][j]+=1
    return visited[i][j]

for i in range(n):
    for j in range(n):
        ans=max(ans,dfs(i,j))

print(ans)
import sys
sys.setrecursionlimit(1000000)
def dfs(i,j):
    visited[i][j]=1
    total=1
    for _ in range(4):
        ny=i+dy[_]
        nx=j+dx[_]
        if 0<=nx<M and 0<=ny<N:
            if board[ny][nx] == 1 and visited[ny][nx]==0:
                total+=dfs(ny,nx)
    return total

dx=[0,0,-1,1]
dy=[-1,1,0,0]
N,M=map(int,input().split())
board=[]
cnt=0
ans=0
visited=[[0]*M for _ in range(N)]

for _ in range(N):
    board.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        if board[i][j]==1 and visited[i][j]==0:
            temp=dfs(i,j)
            if ans < temp:
                ans = temp
            cnt+=1
print(cnt)
print(ans)



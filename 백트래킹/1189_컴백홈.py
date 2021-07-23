def dfs(x,y,d):
    global cnt
    if d==k and x==0 and y==c-1:
        cnt+=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        print(visited)
        if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and board[nx][ny]=='.':
            visited[nx][ny]=1
            dfs(nx,ny,d+1)
            visited[nx][ny]=0


r,c,k=map(int,input().split())
board=[input() for _ in range(r)]
visited=[[0]*c for _ in range(r)]
cnt=0
dx=[0,0,-1,1]
dy=[-1,1,0,0]
visited[r-1][0]=1
dfs(r-1,0,1)
print(cnt)
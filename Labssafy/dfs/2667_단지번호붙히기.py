def dfs(x,y):
    global area
    visited[x][y]=1
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<n and 0<=ny<n:
            if board[nx][ny] == '1' and not visited[nx][ny]:
                area+=1
                dfs(nx,ny)

n=int(input())
board = [input().rstrip() for _ in range(n)]
visited=[[0]*n for _ in range(n)]
cnt=0
ans=[]
for i in range(n):
    for j in range(n):
        area=0
        if board[i][j]!='0' and not visited[i][j]:
            cnt+=1
            dfs(i,j)
            ans.append(area+1)
print(cnt)
ans.sort()
print('\n'.join(map(str,ans)))
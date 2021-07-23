import sys
sys.setrecursionlimit(1000000)
def dfs(i,j,num):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    if len(num)==6:
        if num not in ans:
            ans.append(num)
        return
    for _ in range(4):
        nx=j+dx[_]
        ny=i+dy[_]
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx,ny,num+board[ny][nx])

board=[list(map(str,input().split())) for _ in range(5)]
ans=[]

for i in range(5):
    for j in range(5):
        dfs(i,j,board[i][j])

print(len(ans))
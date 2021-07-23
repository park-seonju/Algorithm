import sys
sys.setrecursionlimit(100000000)
input=sys.stdin.readline

n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
dx=[0,0,-1,1]
dy=[-1,1,0,0]

def dfs(i,j,h):
    visited[i][j]=1
    for _ in range(4):
        nx=i+dx[_]
        ny=j+dy[_]
        if 0<=nx<n and 0<=ny<n and board[nx][ny]>h and not visited[nx][ny]:
            dfs(nx,ny,h)
            
max_num=0
for i in range(n):
    for j in range(n):
        if board[i][j]>max_num:
            max_num=board[i][j] 
ans=1

for h in range(0,max_num): # ans 를 1로 해도 h를 0부터해야함 안그럼 리커젼..
    cnt=0
    visited=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]>h and not visited[i][j]:
                cnt+=1
                dfs(i,j,h)
    if ans<cnt: ans=cnt
print(ans)
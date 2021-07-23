from collections import deque
import sys
input=sys.stdin.readline
y,x=map(int,input().split())
board=[input().rstrip() for _ in range(y)]
dc=[0,0,-1,1]
dr=[-1,1,0,0]
ans=0
for i in range(y):
    for j in range(x):
        if board[i][j]=='L':
            visited=[[0]*x for _ in range(y)]
            q=deque()
            q.append((i,j,0))
            visited[i][j]=1
            while q:
                r,c,cnt=q.popleft()
                if cnt>ans:ans=cnt
                for _ in range(4):
                    nr=r+dr[_]
                    nc=c+dc[_]
                    if 0<=nr<y and 0<=nc<x:
                        if board[nr][nc]=='L' and not visited[nr][nc]:
                            visited[nr][nc]=1
                            q.append((nr,nc,cnt+1))
print(ans)

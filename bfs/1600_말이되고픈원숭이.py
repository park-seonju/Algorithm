from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,-1,1]
dy=[-1,1,0,0]
hx=[-2,-1,1,2,-2,-1,1,2]
hy=[-1,-2,-2,-1,1,2,2,1]

def m_move(i,j,cnt,horse):
    for _ in range(4):
        nx=i+dx[_]
        ny=j+dy[_]
        if 0<=nx<H and 0<=ny<W and (nx,ny,horse) not in visited:
            if board[nx][ny]!=1:
                q.append((nx,ny,cnt+1,horse))
                visited.add((nx,ny,horse))

def h_move(i,j,cnt,horse):
    for _ in range(8):
            nx=i+hx[_]
            ny=j+hy[_]
            if 0<=nx<H and 0<=ny<W and (nx,ny,horse+1) not in visited:
                if board[nx][ny]!=1:
                    q.append((nx,ny,cnt+1,horse+1))
                    visited.add((nx,ny,horse+1))

K=int(input())
W,H=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(H)]

ans=-1
q=deque()
q.append((0,0,0,0)) # i,j,cnt,horse
visited=set((0,0,0)) # i,j,horse

while q:
    i,j,cnt,horse=q.popleft()
    if i==H-1 and j==W-1:
        ans=cnt
        break
    m_move(i,j,cnt,horse)

    if horse<K:
        h_move(i,j,cnt,horse)

print(ans)

    
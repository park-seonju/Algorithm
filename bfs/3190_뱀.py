import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
k=int(input())
board=[[0]*n for _ in range(n)]
direction=[]
ans=0
for _ in range(k):
    i,j=map(int,input().split())
    board[i-1][j-1]=2

L=int(input())
for _ in range(L):
    direction.append(input().split())

dx=[0,1,0,-1] # >방향 : 오른쪽 <방향 : 왼쪽
dy=[1,0,-1,0]

q=deque()
q.append((0,0))
board[0][0]=3

i,j=0,0
way=0
idx=0
while 1:
    i=dx[way]+i
    j=dy[way]+j
    if i<0 or i>=n or j<0 or j>=n or board[i][j]==3:
        ans+=1;break
    if not board[i][j]:
        board[i][j]=3
        q.append((i,j))
        ti,tj=q.popleft()
        board[ti][tj]=0
        ans+=1
    elif board[i][j]==2:
        board[i][j]=3
        q.append((i,j))
        ans+=1
    if direction[idx][0]==str(ans):
        if direction[idx][1]=='L':
            way=(way-1)%4
        elif direction[idx][1]=='D':
            way=(way+1)%4
        idx+=1
print(ans)
# (0 1 0 0 1)/(0 2 0 0 2)/(0 1 0 0 1)

# 0 2 2 0 2 2 2 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0

# 0 0 0 0 0 0
# 0 0 0 0 2 0
# 0 0 0 2 0 0
# 0 0 0 0 0 0
# 0 0 2 0 0 0
# 0 0 0 0 0 0

# 0 0 0 0 0 0 0 1 1 0
# 0 0 0 0 0 0 0 1 1 0
# 0 0 0 0 0 0 0 1 1 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0



# from collections import deque
# Test=int(input())
# for tc in range(1,Test+1):
#     n,m=map(int,input().split())
#     arr=[list(input().rstrip()) for _ in range(n)]
#     board=[[0]*m for _ in range(n)]
#     dx=[0,0,-1,1]
#     dy=[-1,1,0,0]
#     water=[]
#     q=deque()

#     for i in range(n):
#         for j in range(m):
#             if arr[i][j]=='W':
#                 water.append([i,j])

#     for i in range(len(water)):
#         for _ in range(4):
#             nx=dx[_]+water[i][0]
#             ny=dy[_]+water[i][1]
#             if 0<=nx<n and 0<=ny<m and arr[nx][ny]=='L' and board[nx][ny]==0:
#                 board[nx][ny]=1
#                 q.append((nx,ny))
#      # q=물과 인접한 땅에 좌표
#     while q:
#         x,y=q.popleft()
#         for _ in range(4):
#             nx=dx[_]+x
#             ny=dy[_]+y
#             if 0<=nx<n and 0<=ny<m and arr[nx][ny]=='L':
#                 if board[nx][ny]==0:
#                     board[nx][ny] = (board[x][y]+1)
#                     q.append((nx,ny))
#                 else:
#                     if board[nx][ny]>(board[x][y]+1) :
#                         board[nx][ny]=(board[x][y]+1)
#                         q.append((nx,ny))

#     cnt=0
#     for i in range(n):
#         for j in range(m):
#             if board[i][j]!=0:
#                 cnt+=board[i][j]
#     print("#{} {}".format(tc,cnt))

from collections import deque
Test=int(input())
for tc in range(1,Test+1):
    n,m=map(int,input().split())
    arr=[list(input().rstrip()) for _ in range(n)]
    board=[[-1]*m for _ in range(n)]
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    q=deque()

    for i in range(n):
        for j in range(m):
            if arr[i][j]=='W':
                board[i][j]=0
                q.append((i,j))
                
     # q=물과 인접한 땅에 좌표
    while q:
        x,y=q.popleft()
        for _ in range(4):
            nx=dx[_]+x
            ny=dy[_]+y
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]=='L':
                if board[nx][ny]>(board[x][y]+1) :
                    board[nx][ny]=(board[x][y]+1)
                    q.append((nx,ny))
    print(board)
    ans=0
    for i in range(n):
        for j in range(m):
            if board[i][j]!=-1:
                ans+=board[i][j]
    print("#{} {}".format(tc,ans))
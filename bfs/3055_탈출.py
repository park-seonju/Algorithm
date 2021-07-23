from collections import deque
r,c=map(int,input().split())
board=[list(input().rstrip()) for _ in range(r)]
dx=[0,0,-1,1]
dy=[-1,1,0,0]
x,y=0,0
visited=[[0]*c for _ in range(r)]
q=deque()
for i in range(r):
    for j in range(c):
        if board[i][j]=='S':
            q.appendleft([i,j]) #시작지점
        elif board[i][j]=='*':
            q.append([i,j])     #물 지역 출발점
        elif board[i][j]=='D':  # 도착
            x,y=i,j
flag=False
while q:
    if flag:
        break
    nowr,nowc=q.popleft() #시작좌표부터 갈수있는좌표하나씩 뽑고
    for i in range(4):
        nr=nowr+dx[i]
        nc=nowc+dy[i]
        if 0<=nr<r and 0<=nc<c:
            if board[nowr][nowc]=='*':
                if board[nr][nc]=='.' or board[nr][nc]=='S':  
                    board[nr][nc]='*'
                    q.append([nr,nc])
            elif board[nowr][nowc]=='S':
                    if board[nr][nc]=='.':
                        board[nr][nc]='S'
                        visited[nr][nc]=visited[nowr][nowc]+1
                        q.append([nr,nc])
                    elif board[nr][nc]=='D':
                        flag=True
                        visited[nr][nc]=visited[nowr][nowc]+1
                        break
if visited[x][y]==0:
    print('KAKTUS')
else:
    print(visited[x][y])
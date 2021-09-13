from collections import deque
board=[list(input().rstrip()) for _ in range(12)]
ans=0
dx=[0,0,-1,1]
dy=[-1,1,0,0]

def dfs(i,j):
    global bomb
    visited[i][j]=True
    bomb.append((i,j))
    for _ in range(4):
        nx=i+dx[_]
        ny=j+dy[_]
        if 0<=nx<12 and 0<=ny<6:
            if not visited[nx][ny] and board[i][j]==board[nx][ny]:    
                dfs(nx,ny)
while 1:
    bomb=[]
    visited=[[False]*6 for _ in range(12)]
    flag=False
    for i in range(11,-1,-1):
        for j in range(6):
            if not visited[i][j] and board[i][j] != '.':
                dfs(i,j)
                if len(bomb)>=4:
                    for x,y in bomb:
                        board[x][y]='.'
                    flag=True;
                bomb=[]
    if not flag:print(ans);exit()
    for j in range(6):
        temp = deque([])
        for i in range(11,-1,-1):
            if board[i][j]!='.':
                temp.append(board[i][j])
        for i in range(11,-1,-1):
            if temp:
                board[i][j]=temp.popleft()
            else:
                board[i][j]='.'
    ans+=1
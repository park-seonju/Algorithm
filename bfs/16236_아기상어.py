from collections import deque

n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]

dx=[0,-1,0,1]
dy=[-1,0,1,0]
shark,cnt,muk=2,0,0

def bfs(i,j,shark,muk,cnt):
    q,eating=deque(),[]
    q.append((i,j)) #이동할 q
    visited=[[-1]*n for _ in range(n)] #방문 리스트
    visited[i][j]=cnt # 방문체크 겸 이동 카운트로 셈
    while q:
        qlen=len(q)
        while qlen: # 갈수있는좌표의 길이만큼 돌려줌 왜? 같은 깊이에 있는 거 다확인 후 상어 크기키움.
            x,y=q.popleft()
            for _ in range(4):
                nx=x+dx[_]
                ny=y+dy[_]
                if 0<=nx<n and 0<=ny<n and visited[nx][ny]==-1:
                    if board[nx][ny]==0 or board[nx][ny]==shark:
                        visited[nx][ny]=visited[x][y]+1
                        q.append((nx,ny))
                    elif 0<board[nx][ny]<shark:
                        eating.append([nx,ny]) #먹을수 있는좌표 넣어주고
            qlen-=1
        if eating:
            nx,ny=min(eating) # 왼쪽 위에 좌표를 꺼냄
            muk+=1
            if muk==shark:
                muk=0
                shark+=1
            board[nx][ny]=0 #먹었으면 그 자리 0으로 바꿔주고 그자리를 리턴하여 다시 탐색
            return nx,ny,shark,muk,visited[x][y]+1
    print(cnt)
    exit()
                    


for i in range(n):
    for j in range(n):
        if board[i][j]==9:
            x,y=i,j
            board[i][j]=0
while True:
    x,y,shark,cnt,muk=bfs(x,y,shark,cnt,muk)

# a=[[5,5],[4,2],[3,100],[3,1]]
# x,y=min(a)
# print(x,y)
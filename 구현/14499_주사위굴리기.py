n,m,x,y,k=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
move=list(map(int,input().split()))

dice=[0]*7

dx=[0,0,0,-1,1] # X,동,서,북,남
dy=[0,1,-1,0,0] 

for i in range(k):
    way=move[i]
    nx=x+dx[way]
    ny=y+dy[way]
    if 0<=nx<n and 0<=ny<m:
        if way==1: # 동
            dice[1],dice[3],dice[4],dice[6]=dice[4],dice[1],dice[6],dice[3]
        elif way==2: #서
            dice[1],dice[3],dice[4],dice[6]=dice[3],dice[6],dice[1],dice[4]
        elif way==3: #남
            dice[1],dice[2],dice[5],dice[6]=dice[5],dice[1],dice[6],dice[2]
        else: # 북
            dice[1],dice[2],dice[5],dice[6]=dice[2],dice[6],dice[1],dice[5]
        
        if board[nx][ny]==0:
            board[nx][ny]=dice[6]
        else:
            dice[6]=board[nx][ny]
            board[nx][ny]=0
        x=nx
        y=ny
        print(dice[1])
    else:continue
    
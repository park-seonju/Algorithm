# n=int(input())
board=[input().split() for _ in range(4)]
dx=[0,0,-1,1]
dy=[-1,1,0,0]
result=set()
q=[]
for i in range(4):
    for j in range(4):
        q.append((i,j,1,board[i][j]))
        while q:
            x,y,cnt,ans=q.pop()
            if cnt>=7:
                result.add(ans)
                continue
            for _ in range(4):
                nx=dx[_]+x
                ny=dy[_]+y
                if 0<=nx<4 and 0<=ny<4:
                    q.append((nx,ny,cnt+1,ans+board[nx][ny]))
print(len(result))
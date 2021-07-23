# from collections import deque
R,C=map(int,input().split())
board=[list(input().rstrip()) for _ in range(R)]
dx=[0,0,-1,1]
dy=[-1,1,0,0]

ans=1
q=set([(0,0,board[0][0])])
while q:
    i,j,word=q.pop()
    for _ in range(4):
        nx=i+dx[_]
        ny=j+dy[_]
        if 0<=nx<R and 0<=ny<C:
            if board[nx][ny] not in word:
                new_word=word+board[nx][ny]
                q.add((nx,ny,new_word))
                ans=max(ans,len(new_word))
print(ans)

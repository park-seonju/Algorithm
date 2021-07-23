import sys
from collections import deque
input = sys.stdin.readline

Test=int(input())
result=[]

while(Test>0):
    ans=[]
    Test-=1
    L=int(input())
    board=[[0]*L for _ in range(L)]
    que=deque()
    end=[]
    dx=[2,1,-2,-1,-2,-1,2,1]
    dy=[1,2,1,2,-1,-2,-1,-2]
    first=True
    check=[]

    for _ in range(2):
        x,y=map(int,input().split())
        board[x][y]=1
        if first:
            que.append([x,y])
            check.append([x,y])
            first = False
        else:
            end.append([x,y])
    
    while que:
        startX,startY=que.popleft()
        if startX==end[0][0] and startY==end[0][1]:
            ans.append(0)
            break
        for i in range(8):
            nx=startX+dx[i]
            ny=startY+dy[i]
            if 0 <=nx<L and 0 <=ny<L:
                if nx==end[0][0] and ny==end[0][1]:
                    ans.append(board[startX][startY])
                    break
                elif board[nx][ny]==0:
                    board[nx][ny]=board[startX][startY]+1
                    que.append([nx,ny])
                    
    result.append(ans[0])
    print(ans)
for i in result:
    print(i)
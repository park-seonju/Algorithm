from collections import deque
import sys
input=sys.stdin.readline
Test=int(input())
for tc in range(Test):
    n=int(input())
    hx,hy=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(n)]
    fx,fy=map(int,input().split())

    visited=[0 for _ in range(n)]
    result='sad'
    q=deque()
    q.append([hx,hy])
    while q:
        now=q.popleft()
        if abs(now[0]-fx)+abs(now[1]-fy)<=1000:
            result='happy'
            break
        for i in range(n):
            if not visited[i] and (abs(now[0]-arr[i][0])+abs(now[1]-arr[i][1])<=1000):
                visited[i]=1
                q.append(arr[i])
    print(result)



n=int(input())
board=[list(map(int,input().split())) for _ in range(n+2)]
visited=[[999999999]*(n+2) for _ in range(n+2)]
for i in range(n+2):
    for j in range(n+2):
        if i!=j:
            if abs(board[i][0]-board[j][0])+abs(board[i][1]-board[j][1])<=1000:
                visited[i][j]=1
print(board)
print(visited)
for k in range(n+2):
    for x in range(n+2):
        for y in range(n+2):
            visited[x][y]=min(visited[x][y],visited[x][k]+visited[k][y])
if visited[0][n+1]==999999999:
    print('sad')
else:
    print('happy')
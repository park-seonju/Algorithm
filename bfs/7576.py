import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
board = []
que = deque()

for i in range(n) :
    board.append(list(map(int, input().split())))
    for j in range(m) :
        if board[i][j]==1 :
            que.append((i, j, 0))

def isFinished() :
    for i in range(n) :
        for j in range(m) :
            if board[i][j]==0 :
                return False
    return True

ans = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

while que :
    r,c,count = que.popleft()
    for i in range(4) :
        nextR, nextC = r+dr[i], c+dc[i]
        if 0<=nextR<n and 0<=nextC<m and board[nextR][nextC]==0 :
            board[nextR][nextC]=1
            ans = count+1
            que.append((nextR, nextC, ans))


if isFinished() : print(ans)
else : print(-1)
    
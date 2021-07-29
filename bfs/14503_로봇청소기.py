import sys
from collections import deque
input=sys.stdin.readline
N,M = map(int,input().split())
r, c, d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dx = [-1,0,1,0] #북동남서
dy = [0,1,0,-1]

q = deque()
q.append((r,c,d,2))
ans = 0
while q:
    x, y, direction, count = q.popleft()
    next_d = direction
    flag = False
    if board[x][y] == 0:
        board[x][y] = count
    for _ in range(4):
        next_d = (next_d-1) % 4
        nx = x + dx[next_d]
        ny = y + dy[next_d] 
        if board[nx][ny] == 0:
            q.append((nx, ny, next_d, count + 1))
            flag = True
            break

    if not flag:
        backward_dir = (direction-2) % 4
        bx = x + dx[backward_dir]
        by = y + dy[backward_dir]

        if board[bx][by] != 1:
            q.append((bx, by, direction, count))

    ans = count -1

print(ans)
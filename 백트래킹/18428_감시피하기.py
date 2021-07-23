# import sys
# sys.setrecursionlimit(10**8)
# n = int(input())
# board = []
# teacher = []
# for i in range(n):
#     board.append(sys.stdin.readline().split())
#     for j in range(n):
#         if board[i][j]=='T':
#             teacher.append((i,j))
# def check(board):
#     dx = [1,0,-1,0]
#     dy = [0,1,0,-1]
#     for t in teacher:
#         tx,ty = t
#         for d in range(4):
#             nx,ny = tx+dx[d], ty+dy[d]
#             while (0<=nx<n and 0<=ny<n):
#                 if board[nx][ny] == 'S':
#                     return False
#                 elif board[nx][ny] == 'O':
#                     break
#                 nx,ny = nx+dx[d], ny+dy[d]
#     return True

# def dfs(board,n_count,last_x,last_y):
#     if n_count == 0:
#         return check(board)
#     for j in range(last_y,n):
#         if board[last_x][j] =='X':
#             board[last_x][j] = 'O'
#             if dfs(board, n_count-1, last_x, j):
#                 return True
#             board[last_x][j] = 'X'
#     for i in range(last_x,n):
#         for j in range(n):
#             if board[i][j]=='X':
#                 board[i][j] = 'O'
#                 if dfs(board, n_count-1, i,j):
#                     return True
#                 board[i][j] = 'X'
#     return False

# if dfs(board,3,0,0): print('YES')
# else: print('NO')

from itertools import combinations as cb


def watch():
    for teacher in teacher_list:
        x, y = teacher
        # 상
        nx, ny = x, y
        while nx > 0:
            nx -= 1
            if hallway[nx][ny] == 'S':
                return False

            if hallway[nx][ny] == 'O':
                break
        # 하
        nx, ny = x, y
        while nx < N - 1:
            nx += 1
            if hallway[nx][ny] == 'S':
                return False
            if hallway[nx][ny] == 'O':
                break
        # 좌
        nx, ny = x, y
        while ny > 0:
            ny -= 1
            if hallway[nx][ny] == 'S':
                return False
            if hallway[nx][ny] == 'O':
                break
        # 우
        nx, ny = x, y
        while ny < N - 1:
            ny += 1
            if hallway[nx][ny] == 'S':
                return False
            if hallway[nx][ny] == 'O':
                break
    return True


if __name__ == '__main__':
    N = int(input())
    hallway = [input().split() for _ in range(N)]

    empty_list = []
    teacher_list = []
    for i in range(N):
        for j in range(N):
            if hallway[i][j] == 'X':
                empty_list.append((i, j))
            elif hallway[i][j] == 'T':
                teacher_list.append((i, j))
    print('empty',empty_list)
    # 벽 3개 뽑기
    for walls in cb(empty_list, 3):
        print(walls)
        # 벽 세우기
        for wall in walls:
            x, y = wall
            hallway[x][y] = 'O'
        # 감시하기
        if watch():
            print('YES')
            break
        # 벽 허물기
        for wall in walls:
            x, y = wall
            hallway[x][y] = 'X'
    else:
        print('NO')


import sys

input = sys.stdin.readline

n = int(input())
board = [["O"]*(n+2)]+[["O"]+list(input().split())+["O"] for _ in range(n)]+[["O"]*(n+2)]
teacher = []
for i in range(1, n+1):
    for j in range(1, n+1):
        if board[i][j] == "T":
            teacher.append((i, j))
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
lines = []  # 학생을 볼 수 있는 복도 리스트

for r, c in teacher:
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        line = []
        while board[nr][nc] == "X":  # 빈공간이 아닐 때까지 탐색
            line.append((nr, nc))
            nr, nc = nr+dr[i], nc+dc[i]
        if board[nr][nc] == "S":  # 탐색이 끝난 지점이 학생이면 복도 리스트에 append
            lines.append(line)

lines.sort(key = lambda x: len(x))
count = 0
while lines and count<3:  # 남은 복도가 없거나 세번 지울때까지 반복
    now = lines[0]
    if len(now)==0: break  # 만약 복도의 길이가 0인경우 불가능하므로 break
    maxL = []
    for block1 in now:  # 해당 복도가 다른 복도들과 겹치는 지점이 있으면 tmp에 추가
        tmp = [0]
        for i in range(1, len(lines)): 
            for block2 in lines[i]:
                if block1==block2:
                    tmp.append(i)
                    break
        if len(maxL) < len(tmp):
            maxL = tmp
    for i in maxL[::-1]:  # 가장 많이 겹치는 복도들 삭제
        lines.pop(i)
    count += 1

if lines:
    print("NO")
else: print("YES")
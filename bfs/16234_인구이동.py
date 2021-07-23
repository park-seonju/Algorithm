import sys
sys.setrecursionlimit(1000000)

n,l,r = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
count = 0

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and check[nx][ny]:
            temp = abs(country[x][y] - country[nx][ny])
            if l <= temp <= r:
                check[nx][ny] = False
                stack.append([nx, ny])
                dfs(nx, ny)



while True:
    check = [[True] * n for _ in range(n)]  # True false 반대로 하면 왜 recursion에러??
    flag = True # while문 빠져나가기위함
    for i in range(n):
        for j in range(n):
            stack = []
            if check[i][j]:
                stack.append([i, j])
                check[i][j] = False
                dfs(i, j)
                if len(stack) > 1:
                    flag = False #연합이 존재하므로 반복
                    avg = sum([country[x][y] for x, y in stack]) // len(stack)
                    for x, y in stack:
                        country[x][y] = avg

    if flag:
        break

    count += 1

print(count)
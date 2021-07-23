from collections import deque

M, N, K = map(int, input().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

graph = [list([0] * N) for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1,y2):    # 행은 세로의 갯수 이므로 y
        for j in range(x1, x2):  # 열은 가로의 갯수 이므로 x
            graph[i][j] = 2
print(graph)
resultList = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            count = 1
            queue = deque([])   # deque리스트 만들고
            queue.append([i, j]) # 그 위치를 저장
            graph[i][j] = count  # 그위치를 1로 채움.

            while queue:
                y, x = queue.popleft()
                for k in range(4):
                    nY = y + dy[k]
                    nX = x + dx[k]

                    if 0 <= nX < N and 0 <= nY < M and graph[nY][nX] == 0:   # 빈 곳이면
                        graph[nY][nX] = 1    #1로 채워주고
                        queue.append([nY, nX])   # 빈 좌표를 넣어줌
                        count += 1  #갯수를 세야하므로 count + 1

            resultList.append(count)

print(len(resultList))
resultList.sort()
for num in resultList:
    print(num,end=" ") 
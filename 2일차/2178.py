import sys

n,m = map(int, sys.stdin.readline().split())

board=[]

for i in range(n) :
    board.append(list(map(int, sys.stdin.readline().strip())))

q = [(0,0,1)] 
visited = [[0 for _ in range(m)] for _ in range(n)]
dr = [0, 1, 0, -1] # 오른쪽, 아래, 왼쪽, 위쪽
dc = [1, 0, -1, 0]

while q :
    now = q.pop()

    for i in range(4) :
        
        nextR, nextC = now[0]+dr[i],now[1]+dc[i]
        
        if 0<=nextR<n and 0<=nextC<m and visited[nextR][nextC]==0 and board[nextR][nextC]==0 :
            q = [(nextR,nextC,now[2]+1)]+q
            visited[nextR][nextC]=now[2]+1
print(visited)
print(visited[n-1][m-1])
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = []
virus = []
empty = []

for i in range(n) :
    board.append(list(map(int, input().split())))
    for j,a in enumerate(board[i]) :
        if a==2 : virus.append((i,j))
        elif a==0 : empty.append((i,j))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
ans = 0

for i in range(len(empty)) :
    board[empty[i][0]][empty[i][1]]=1
    for j in range(i+1,len(empty)) :
        board[empty[j][0]][empty[j][1]]=1
        for k in range(j+1,len(empty)) :
            board[empty[k][0]][empty[k][1]]=1

            visited = [ [ 0 for _ in range(m)] for _ in range(n) ]
            que = deque(virus)

            count=len(empty)-3
            
            while que :
                r, c = que.popleft()
                for p in range(4) :
                    nextR, nextC = r+dr[p], c+dc[p]
                    if 0<=nextR<n and 0<=nextC<m and not visited[nextR][nextC] and not board[nextR][nextC] :
                        count-=1
                        visited[nextR][nextC]=1
                        que.append((nextR,nextC))
                        
            ans = max(ans, count)

            board[empty[k][0]][empty[k][1]]=0
        board[empty[j][0]][empty[j][1]]=0
    board[empty[i][0]][empty[i][1]]=0

print(ans)


'''
board = [][][][]...

empty = []

def combi(next, count) :

    if count==3 :        # 몇개골랐는지 세는것
        # bfs

    for a in range(next, len(empty)) :
        visited[a]=1   # 뭘 몰랐는지 체크
        combi(a+1, count+1)
        visited[a]=0

combi(0,0)
'''
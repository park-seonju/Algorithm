import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)  #  최대 재귀의 깊이를 늘려줌.

T = int(input())
result=[]

for _ in range(T):
    M,N,K =  map(int, input().split())

    board = [[0 for _ in range(N)] for _ in range(M)]  #안에가 열 밖이 행

    for _ in range(K) :
        i,j=(map(int, input().split()))
        board[i][j]=1

    visited = [[0 for _ in range(N)] for _ in range(M)]

    dr = [1,-1,0,0]
    dc = [0,0,-1,1]

    def dfs(r, c) :
        
        visited[r][c] = 1
        
        for i in range(4) :
            nextR = r+dr[i]
            nextC = c+dc[i]
            
            if 0<=nextR<M and 0<=nextC<N :
                if visited[nextR][nextC]==0 and board[nextR][nextC]==1 :
                    dfs(nextR,nextC)

    ans = []

    for i in range(M) :
        for j in range(N) :
            if board[i][j]==1 and visited[i][j]==0 :
                ans.append(dfs(i,j))
    result.append(len(ans))
print(ans)
for i in range(len(result)):
    print(result[i])
    
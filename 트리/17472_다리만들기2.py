import sys
sys.setrecursionlimit(10**6)

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def dfs(x,y,num):
    visited[x][y]=1
    board[x][y]=num
    for _ in range(4):
        nx=x+dx[_]
        ny=y+dy[_]
        if 0<=nx<n and 0<=ny<m:
            if board[nx][ny] and not visited[nx][ny]:        
                dfs(nx,ny,num)

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
visited=[[0 for mm in range(m)] for nn in range(n)]

naming=1
for i in range(n):
    for j in range(m):
        if board[i][j] and not visited[i][j]:
            dfs(i,j,naming)
            naming+=1



# import sys

# input = sys.stdin.readline

# def find(a):
#     if uf[a]==a: return a
#     uf[a] = find(uf[a])
#     return uf[a]

# def union(a, b):
#     aa = find(a)
#     bb = find(b)
#     if aa > bb: uf[a] = bb
#     else: uf[b] = aa

# def dfs(r, c):
#     board[r][c] = num
#     if board[r+1][c]==1: dfs(r+1,c)
#     if board[r][c+1]==1: dfs(r,c+1)
#     if board[r-1][c]==1: dfs(r-1,c)
#     if board[r][c-1]==1: dfs(r,c-1)

# n, m = map(int, input().split())

# board = [[0]*(m+2)]+[[0]+list(map(int,input().split()))+[0] for _ in range(n)]+[[0]*(m+2)]

# num = 2
# for r in range(1, n+1):
#     for c in range(1, m+1):
#         if board[r][c] == 1:
#             dfs(r, c)
#             num += 1

# link = []
# for i in range(1, n+1):
#     c = 1
#     cnt = 0
#     island = board[i][c]
#     while c<=m:
#         if board[i][c] == 0:
#             cnt += 1
#         elif island and island != board[i][c]:
#             if cnt > 1: link.append((cnt, island, board[i][c]))
#             island = board[i][c]
#             cnt = 0
#         else: 
#             island = board[i][c]
#             cnt = 0
#         c += 1

# for i in range(1, m+1):
#     r = 1
#     cnt = 0
#     island = board[r][i]
#     while r<=n:
#         if board[r][i] == 0:
#             cnt += 1
#         elif island and island != board[r][i]:
#             if cnt > 1: link.append((cnt, island, board[r][i]))
#             island = board[r][i]
#             cnt = 0
#         else: 
#             island = board[r][i]
#             cnt = 0
#         r += 1

# uf = [i for i in range(num)]

# link.sort(key = lambda x: x[0])
# cnt = ans = 0
# MAX = num-3
# for d, a, b in link:
#     if find(a) != find(b):
#         union(uf[a], uf[b])
#         cnt += 1
#         ans += d
#         if cnt == MAX: break

# if cnt != MAX: print(-1)
# else: print(ans)
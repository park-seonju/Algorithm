import sys
sys.setrecursionlimit(10**6)
input= sys.stdin.readline

def dfs(n):  # 연결 부분을 확인하는부분
  visited[n]=True
  for i in matrix[n]:  # 첫번째 매트릭스 부터 탐색
    if not visited[i]:
      dfs(i)

n, m = map(int, input().split())

matrix = [ [] for _ in range(n+1)]

for _ in range(m):
  u, v = map(int, input().split())
  matrix[u].append(v)
  matrix[v].append(u)
  
visited = [False]*(n+1)
cnt = 0

print('first matrix',matrix)
print('visited',visited)


for i in range(1, n+1):   # N번만큼 반복
  if not visited[i]:
    cnt+=1
    dfs(i)

print(cnt)

# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
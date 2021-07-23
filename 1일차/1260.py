import sys
#sys.stdin.readline() = input()
N,M,V=map(int,input().split())
matrix=[[0]*(N+1) for i in range(N+1)]  # 0행 0열은 왜 추가??
for i in range(M):
    a,b = map(int,input().split())
    matrix[a][b]=matrix[b][a]=1
visit_list=[0]*(N+1)

def dfs(V):
    visit_list[V]=1 #방문한 점 1로 표시
    print(V, end=' ')
    for i in range(1,N+1):
        if(visit_list[i]==0 and matrix[V][i]==1):
            dfs(i)

def bfs(V):
    queue=[V] #들려야 할 정점 저장
    visit_list[V]=0 #방문한 점 0으로 표시
    while queue:
        V=queue.pop(0)  #1.2.4.3  
        print(V, end=' ')
        for i in range(1, N+1):
            if(visit_list[i]==1 and matrix[V][i]==1):
                queue.append(i)
                visit_list[i]=0

dfs(V)
print()
bfs(V)

'''
import sys

def dfs(i) :
    if visited[i] : return
    visited[i]=True
    ans.append(i)
    for j in graph[i] :
        dfs(j)



n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m) :
    a,b = map(int,  sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)

for a in graph :
    a.sort()
ans=[]



dfs(v)
print(*ans)

ans=[]
visited = [False for _ in range(n+1)]

que = [v]
while que :
    next = que.pop()
    if visited[next] : continue
    visited[next]=True
    ans.append(next)
    for i in graph[next] :
        que = [i]+que

print(' '.join(map(str,ans)))

'''
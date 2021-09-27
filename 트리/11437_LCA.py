import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n=int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    n1,n2 = map(int,input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)
parent = [0]*(n+1)
visited=[False]*(n+1)
d=[0]*(n+1) # 깊이 저장 d 리스트
def dfs(node,depth):
    visited[node]=True
    d[node]=depth
    for e in adj[node]:
        if not visited[e]:
            parent[e]=node #부모 정보 갱신
            dfs(e,depth+1)
dfs(1,0)

def LCA(a,b):
    while d[a]!=d[b]: # 깊이가 다르면
        if d[a]>d[b]: # 깊이가 큰쪽을
            a=parent[a] # 부모깊이로 낮춰준다.(위로땡긴다)
        else:
            b=parent[b]
    while a!=b: # 노드가 같아질때까지
        a=parent[a] #부모방향으로
        b=parent[b] #동시이동
    return a

m=int(input())

for _ in range(m):
    f1,f2=map(int,input().split())
    print(LCA(f1,f2))

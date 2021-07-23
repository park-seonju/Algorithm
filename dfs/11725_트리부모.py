# N=int(input())
# New=N+1
# adj=[[] for _ in range(New)]
# visited=[0]*New
# for _ in range(N-1):
#     s,e=map(int,input().split())
#     if visited[e] == 0:
#         if e==1:
#             adj[1].append(s)
#             visited[s]=1
#             continue
#         adj[s].append(e)
#         visited[e]=1
#     else:
#         adj[e].append(s)
#         visited[s]=1
# ans=[]
# k=2
# while N-1>0:
#     N-=1
#     for i in range(New):
#         if not adj[i]:
#             continue
#         if k in adj[i]:
#             ans.append(i)
#             k+=1
#             break
# for i in ans:
#     print(i)
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

N=int(input())
New=N+1
adj=[[] for _ in range(New)]
visited=[0 for _ in range(New)]

def dfs(n):
    for i in adj[n]:
        if not visited[i]:
            visited[i]=n
            dfs(i)

for _ in range(N-1):
    s,e=map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)

dfs(1)
# while to_visit:
#     now=to_visit.pop()
#     for i in adj[now]:
#         if not visited[i]:
#             visited[i]=1
#             ans[i]=now
#             to_visit.append(i)
for i in range(2,New):
    print(visited[i])
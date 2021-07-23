# import sys

# input = sys.stdin.readline
# tc = int(input())
# for _ in range(tc):
#     n,m,w=map(int,input().split())

#     graph = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]
#     for i in range(1, n+1):
#         graph[i][i] = 0

#     for i in range(m):
#         s, e, c = map(int, input().split())
#         if c < graph[s][e]:
#             graph[s][e] = c
#             graph[e][s] = c

#     for i in range(w):
#         s, e, c = map(int, input().split())
#         if -c < graph[s][e]:
#             graph[s][e] = -c

#     for k in range(1, n+1):
#         for s in range(1, n+1):
#             for e in range(1, n+1):
#                 if graph[s][e] > graph[s][k] + graph[k][e]:
#                     graph[s][e] = graph[s][k] + graph[k][e]

#     flag=False

#     for i in range(1, n+1):
#         if graph[i][i] < 0: flag=True;break
#     if flag:print('YES')
#     else:print('NO')

import sys
input=sys.stdin.readline
T=int(input())
for tc in range(T):
    n,m,w=map(int,input().split())
    adj=[]
    for _ in range(m):
        s,e,t=map(int,input().split())
        adj.append([s,e,t])
        adj.append([e,s,t])
 
    for _ in range(w):
        s,e,t=map(int,input().split())
        adj.append([s,e,-t])
 
    INF=sys.maxsize
 
    result = [INF]*(n + 1)
    result[1] = 0
    flag=False
    for i in range(n):
        for info in adj:
            s=info[0]
            e=info[1]
            t=info[2]
            if result[e]>t+result[s]:
                result[e]=t+result[s]
                if i==n-1:
                    flag=True
 
    if flag:
        print("YES")
    else:
        print("NO")
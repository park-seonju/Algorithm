import sys
input=sys.stdin.readline
n,m=map(int,input().split())
adj={i+1:[] for i in range(n)}
INF=sys.maxsize
result=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    adj[a].append((c,b))

result[1]=0
flag=False

for i in range(n):
    for node in adj.keys():
        if result[node] != INF:
            for next_time,next_node in adj[node]:
                if result[next_node]>result[node]+next_time:
                    result[next_node]=result[node]+next_time
                    if i==n-1:flag=True

if flag: print(-1)
else:
    ans=[]
    for i in result[2:]:
        print(i if i!=INF else -1)
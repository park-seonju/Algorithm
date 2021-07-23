def dfs(s,nodedistlist):
    for e,d in adj[s]:
        if not nodedistlist[e]:
            nodedistlist[e]=d+nodedistlist[s]
            dfs(e,nodedistlist)
v=int(input())
adj=[[] for _ in range(v+1)]
for _ in range(v):
    inputs=list(map(int,input().split()))
    for i in range(1,len(inputs)-1,2):
        adj[inputs[0]].append((inputs[i],inputs[i+1]))

dist=[0 for _ in range(v+1)]
dfs(1,dist)
dist[1]=0

maximum=0
node=0

# 임의로 시작 한 노드(1로해줬음) 들의 거리중 최대 거리값과 도착 노드를 구함
for i in range(v+1):
    if maximum<dist[i]:
        maximum=dist[i]
        node=i

# 근데 왜 가장 긴 지점에서 다시 dfs를 해서 구하는거지?
result=[0 for _ in range(v+1)]
dfs(node,result)
result[node]=0
print(max(result))

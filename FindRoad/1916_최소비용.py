import heapq
n=int(input())
m=int(input())

adj=[[] for _ in range(n+1)]
ans=[999999999]*(n+1)

for _ in range(m):
    s,e,w=map(int,input().split())
    adj[s].append((w,e))

start,end=map(int,input().split())
ans[start]=0

heap=[]
heapq.heappush(heap,(0,start))

while heap:
    weight,now=heapq.heappop(heap)
    if ans[now]<weight: continue;
    for w,next_node in adj[now]:
        next_weight=w+weight
        if next_weight < ans[next_node]:
            ans[next_node]=next_weight
            heapq.heappush(heap,(next_weight,next_node))
print(ans[end])

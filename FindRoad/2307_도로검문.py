import heapq,sys
input=sys.stdin.readline
n,m=map(int,input().split())
adj=[[] for _ in range(n+1)]
road=[]
ans=[999999999]*(n+1)

for _ in range(m):
    a,b,t=map(int,input().split())
    adj[a].append((t,b))
    adj[b].append((t,a))
    road.append((a,b,t))
heap=[]
ans[1]=0
heapq.heappush(heap,(0,1))
while heap:
    weight,now=heapq.heappop(heap)
    if ans[now]<weight: continue;
    for w,next_node in adj[now]:
        next_weight=w+weight
        if next_weight < ans[next_node]:
            ans[next_node]=next_weight
            heapq.heappush(heap,(next_weight,next_node))

base=ans[n]
result=-1
# a= road[0][0] b=road[0][1] t=road[0][2]
wow=0
while wow<m:
    ans=[999999999]*(n+1)
    ans[1]=0   
    # adj[a].remove((t,b))
    # adj[b].remove((t,a))
    heapq.heappush(heap,(0,1))
    while heap:
        weight,now=heapq.heappop(heap)
        if ans[now]<weight: continue;
        for w,next_node in adj[now]:
            if w==road[wow][2] and (next_node==road[wow][0] or next_node==road[wow][1]):continue
            next_weight=w+weight
            if next_weight < ans[next_node]:
                ans[next_node]=next_weight
                heapq.heappush(heap,(next_weight,next_node))
    if base<=ans[n]:
        temp=ans[n]-base
        if result < temp:
            result=temp
    # adj[a].append((t,b))
    # adj[b].append((t,a))
    wow+=1
if result==(999999999-base):print(-1)
else:print(result)


import sys, heapq

input = sys.stdin.readline

def djt(s, e):
    time = [MAX_TIME for _ in range(n+1)]
    time[1] = 0
    heap = [(0, 1)]
    while heap:
        t, now = heapq.heappop(heap)
        if now==n: break
        for next, plus in graph[now]:
            if s==now and e==next or s==next and e==now: continue
            if t+plus < time[next]:
                time[next] = t+plus
                if not s: pre[next] = now
                heapq.heappush(heap, (time[next], next))
    return time[n]

MAX_TIME = 10000000
        
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b,t))
    graph[b].append((a,t))

pre = [0 for _ in range(n+1)]

result = djt(0,0)

ans = -1
e = n
while pre[e]!=0:
    s = pre[e]
    tmp = djt(s, e)
    if tmp != MAX_TIME:
        tmp = tmp-result
        ans = max(ans, tmp)
    else:
        ans = -1
        break
    e = s
print(ans)
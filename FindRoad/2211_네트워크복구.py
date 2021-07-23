import heapq,sys
input=sys.stdin.readline
INF=sys.maxsize
n,m=map(int,input().split())
adj=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))

heap=[]
heapq.heappush(heap,(0,1))
ans=[INF]*(n+1)
result=[0 for _ in range(n+1)]
ans[1]=0

while heap:
    w,com=heapq.heappop(heap)
    if ans[com]<w: continue;
    for next_com,next_w in adj[com]:
        next_weight=w+next_w
        if next_weight < ans[next_com]:
            ans[next_com]=next_weight
            result[next_com]=com
            heapq.heappush(heap,(next_weight,next_com))

print(n - 1) # ? 왜 n-1 이지
for i in range(2,n+1):
    print(i,result[i])
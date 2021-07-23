import heapq,sys
input=sys.stdin.readline
tc=int(input())
for test in range(tc):
    INF=sys.maxsize
    n,d,c=map(int,input().split())
    adj=[[] for _ in range(n+1)]
    dist=[INF]*(n+1)
    for _ in range(d):
        a,b,s=map(int,input().split())
        adj[b].append((a,s))
    heap=[]
    heapq.heappush(heap,(0,c))
    dist[c]=0
    while heap:
        time,com=heapq.heappop(heap) 
        if dist[com]<time:continue
        for next_com,nt in adj[com]:
            next_time=nt+time
            if dist[next_com]>next_time:
                dist[next_com]=next_time
                heapq.heappush(heap,(next_time,next_com))
    cnt=0
    sec=0
    for i in dist:
        if i!=INF:
            cnt+=1
            sec=max(sec,i)
    print(cnt,sec)




import heapq,sys
input=sys.stdin.readline
tc=int(input())
for test in range(tc):
    INF=sys.maxsize
    n,d,c=map(int,input().split())
    adj=[[] for _ in range(n+1)]
    dist=[INF]*(n+1)
    for _ in range(d):
        a,b,s=map(int,input().split())
        adj[b].append((a,s))
    heap=[]
    heapq.heappush(heap,(0,c,1))
    count=0
    dist[c]=0
    while heap:
        time,com,cnt=heapq.heappop(heap)
        if dist[com]<time:continue
        for next_com,nt in adj[com]:
            next_time=nt+time
            if dist[next_com]>next_time:
                dist[next_com]=next_time
                count=cnt+1
                heapq.heappush(heap,(next_time,next_com,cnt+1))
    sec=0
    for i in dist:
        if i!=INF:
            sec=max(sec,i)
    print(count,sec)
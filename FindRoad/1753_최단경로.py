import sys
input=sys.stdin.readline

v,e=map(int,input().split())
start=int(input())
adj=[[] for _ in range(v+1)]

for _ in range(e):
    s,e,w=map(int,input().split())
    adj[s].append((e,w)) # 정점 index에 도착점,가중치

ans=[-1 for _ in range(v+1)]
visited=[False for _ in range(v+1)]

ans[start]=0
min_num=0  # 연결된 정점중 가중치 제일 작은 수

while True:
    visited[start]=True
    for s,w in adj[start]:
        if ans[start]==0: #맨 처음 점이고
            if ans[s] != -1 and ans[s] > w: #같은 방향의 다른가중치 점이면 가중치 작은거 넣어줌
                ans[s]=w; continue;
            elif ans[s] == -1: ans[s]=w; continue; # 그냥넣어줌
        if ans[s]>w+min_num:  # 그곳 가중치가 지나온 점가중치의합보다 크면 바꿔줌
            ans[s]=w+min_num
        else: #만약 그게 아니면 그대로 냅둬야하는데
            if ans[s]==-1: ans[s]=w+min_num # 처음 가는 곳이면 그냥 더한 것 넣어줌
    temp=[i for i in range(1,v+1) if ans[i]!=-1 and not visited[i]] # ans에 있는 수 중 -1, 0 아닌 것 뽑아서 
    if not temp: break;
    min_num=11 
    for i in temp:
        if min_num>ans[i]:min_num=ans[i];start=i; #temp 안에 수중 가장 작은 거 뽑고 인덱스 start로 저장
for i in ans[1:]:
    if i==-1: print('INF');
    else: print(i);


import heapq
import sys
input=sys.stdin.readline
v,e=map(int,input().split())
start=int(input())
ans=[999999999]*(v+1)
heap=[]
adj=[[] for _ in range(v+1)]
for _ in range(e):
    s,e,w=map(int,input().split())
    adj[s].append((w,e))

ans[start]=0
heapq.heappush(heap,(0,start))

while heap:
    weigh,now=heapq.heappop(heap)
    if ans[now]<weigh:continue; #현재갈수있는 거리보다 크면 무시
    for w,next_node in adj[now]:
        next_w=w+weigh
        if next_w<ans[next_node]:
            ans[next_node]=next_w
            heapq.heappush(heap,(next_w,next_node))

for i in range(1,v+1):
    if ans[i]==999999999:
        print('INF')
    else:
        print(ans[i])
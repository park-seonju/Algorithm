def dfs(arr,i):
    global count
    global visited  # 방문 한지 안한지도 글로벌로 선언.
    visited[i]=1
    for e in arr[i]:
        if not visited[e]:
            count+=1
            dfs(arr,e)


N,M=map(int,input().split())
heavy=[[] for _ in range(N+1)]
light=[[] for _ in range(N+1)]
mid=int((N+1)//2)
for _ in range(M):
    a,b=map(int,input().split())
    heavy[b].append(a)
    light[a].append(b)
ans=0
for i in range(1,N+1):
    visited = [0] * (N + 1) #방문한지 안한지는 1,2,3번 구슬~ 다 초기화 해줘야함
    count = 0
    dfs(heavy,i)
    if count>=mid: # 1번 구슬부터 끝까지 탐색하여 mid 보다 무겁거나 가벼운게 많으면 ans+1
        ans+=1
    count=0
    dfs(light,i)
    if count>=mid:
        ans+=1
print(ans)
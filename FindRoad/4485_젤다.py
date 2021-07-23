import heapq
n=1
num=1
while n != 0:
    n=int(input())
    if n==0: break;
    board=[list(map(int,input().split())) for _ in range(n)]
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    visited=[[0]*n for _ in range(n)]
    visited[0][0]=1
    ans=999999999
    heap=[]
    heapq.heappush(heap,(board[0][0],0,0))
    while heap:
        weight,i,j=heapq.heappop(heap)
        if i==n-1 and j==n-1:
            ans=weight;break;
        for _ in range(4):
            nx=i+dx[_]
            ny=j+dy[_]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                visited[nx][ny]=1
                heapq.heappush(heap,(weight+board[nx][ny],nx,ny))
    print("Problem {}: {}".format(num,ans))
    num+=1
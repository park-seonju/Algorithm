import heapq,sys
input=sys.stdin.readline
m,n=map(int,input().split())
board=[list(input()) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
visited[0][0]=1
dx=[0,0,-1,1]
dy=[-1,1,0,0]
heap=[]
heapq.heappush(heap,(0,0,0))
while heap:
    cnt,i,j=heapq.heappop(heap)
    if i == n-1 and j == m-1:
        print(cnt);break
    for _ in range(4):
        nx= i+dx[_]
        ny= j+dy[_]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny]=1
            if board[nx][ny]=='1':
                heapq.heappush(heap,(cnt+1,nx,ny))
            else:
                heapq.heappush(heap,(cnt,nx,ny))
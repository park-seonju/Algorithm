import sys
from itertools import combinations
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
chicken=[]
house=[]
ans=999999999
for i in range(n):
    for j in range(n):
        if board[i][j]==2:
            chicken.append((i,j))
        if board[i][j]==1:
            house.append((i,j))
for x in combinations(chicken,m):
    result=0
    q=deque(house)
    while q:
        temp=999999999
        i,j=q.popleft()
        for r,c in x:
            temp=min(temp,abs(i-r)+abs(j-c))
        result+=temp
    ans=min(ans,result)
print(ans)

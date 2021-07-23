import sys
from collections import deque

input=sys.stdin.readline
n,m=map(int,input().split())
arr=list(map(int,input().split()))
s=max(arr)
e=sum(arr)
while s<=e:
    mid = (s+e)//2
    cnt=1 # 블루레이 갯수
    total=0
    for i in arr:
        if total+i>mid:
            cnt+=1
            total=0
        total+=i
    if cnt<=m: # 갯수가 주어진거보다 적으면 기준 내려서 세세하게 들어가게끔
        e=mid-1
    else: # 카운트가 더 많으면 기준을 올려서 많이들어가게끔
        s=mid+1
print(s)
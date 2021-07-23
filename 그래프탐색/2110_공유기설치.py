import sys
input=sys.stdin.readline
n,c=map(int,input().split())
arr=[int(input()) for _ in range(n)]
arr.sort()
s=1
e=arr[-1]
ans=0
if c==2:
    print(arr[-1]-arr[0])
else:
    while s<=e:
        mid=(s+e)//2
        cnt=1
        first=arr[0]
        for i in range(1,n):
            if arr[i]-first>=mid: # ?
                cnt+=1
                first=arr[i]
        if cnt>=c:
            ans=max(mid,ans)
            s=mid+1
        else:
            e=mid-1
    print(ans)
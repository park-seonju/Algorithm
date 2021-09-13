k,n=map(int,input().split())
arr=[int(input()) for _ in range(k)]
arr.sort()
maximum=arr[-1]
e=arr[-1]
s=1
ans=0
while s<=e:
    mid=(s+e)//2
    total=sum(i//mid for i in arr)
    if total>=n:
        ans=max(ans,mid)
        s=mid+1
    else:
        e=mid-1
print(ans)
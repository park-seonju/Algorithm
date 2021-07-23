n,m=map(int,input().split())
arr=list(map(int,input().split()))
s=1
e=max(arr)
ans=0
if n==1:
    print(arr[0]-m)
    exit()
while s<=e:
    mid=(s+e)//2
    total=sum(i-mid if i>mid else 0 for i in arr) # 시간단축
    if total>=m:
        ans=max(ans,mid)
        s=mid+1
    else:
        e=mid-1
print(ans)

# pypy
n,m=map(int,input().split())
arr=list(map(int,input().split()))
maximum=max(arr)
s=1
e=maximum
ans=0
if n==1:
    print(arr[0]-m)
    exit()
while s<=e:
    mid=(s+e)//2
    total=0
    for i in range(n):
        wood=arr[i]-mid
        if 0<wood<maximum:
            total+=wood
    if total>=m:
        ans=max(ans,mid)
        s=mid+1
    else:
        e=mid-1
print(ans)

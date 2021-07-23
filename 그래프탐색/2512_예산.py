n=int(input())
arr=list(map(int,input().split()))
m=int(input())
s=1
e=max(arr) # 처음 m을 e 로 뒀는데 틀림 이유?
ans=0
while s<=e:
    mid=(s+e)//2
    total=sum(i if mid>i else mid for i in arr)
    # 밑에 if문 기준은?
    if total<=m:
        ans=mid
        s=mid+1
    else:
        e=mid-1
print(ans)
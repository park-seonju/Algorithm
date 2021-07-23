n=int(input())
arr=list(map(int,input().split()))
dp=[0]*n
dp[0]=arr[0]
for i in range(1,n):
    dp[i]=arr[i]
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[i],arr[i]+dp[j]) # 전까지 저장한것합 or 그 자체숫자
print(max(dp))

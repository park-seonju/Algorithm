n=int(input())
arr=list(map(int,input().split()))
dp=[1]*n
for i in range(1,n):
    temp=0
    for j in range(i):
        if arr[i]<arr[j]:
            temp=max(temp,dp[j])
    dp[i]=temp+1
print(max(dp))

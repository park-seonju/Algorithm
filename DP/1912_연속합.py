n=int(input())
arr=list(map(int,input().split()))
dp=[0]*n
dp[n-1]=arr[n-1]
for i in range(n-1,0,-1):
    cal=arr[i-1]+dp[i]
    dp[i-1]=max(cal,arr[i-1])
print(max(dp))
n=int(input())
arr=[0]+list(map(int, input().split()))
dp=[0]*(n+1)
for i in range(1, n+1):
    for j in range(1, i+1):
        # 현재 dp 값과 현재 arr 값+ 이전까지의 dp 값 중 max
        dp[i] = max(dp[i], arr[j] + dp[i-j])
print(dp[n])
n=int(input())
arr=list(map(int,input().split()))
dp=[1]*(n)
for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]:
            # 자기 dp[i] 가 큰지 비교하는 숫자들 +1 이 큰지
            dp[i]=max(dp[j]+1,dp[i]) 
print(max(dp))
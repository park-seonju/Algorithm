n=int(input())
dp=[0]*(n+1)
idx=0
while idx<n:
    idx+=1
    if idx==1:
        dp[idx]=0;continue
    dp[idx]=dp[idx-1]+1
    if idx%3==0 and dp[idx]>dp[idx//3]+1:
        dp[idx]=dp[idx//3]+1
    elif idx%2==0 and dp[idx]>dp[idx//2]+1:
        dp[idx]=dp[idx//2]+1
print(dp[n])
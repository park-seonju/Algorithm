n=int(input())
# print('SK' if n%2 else 'CY')
if n==1 or n==3:print('SK');exit()
elif n==2 or n==4:print('CY');exit()
else:
    dp=[-1]*1010
    dp[0]=0
    dp[1]=1
    dp[2]=0
    dp[3]=1
    for i in range(4,n+1):
        if min(dp[i-1],dp[i-3])==1: #의미없음 차피 이기고 지고 둘중하나니까
            dp[i]=0
        else:dp[i]=1
    if dp[n]==1:print('SK')
    else:print('CY')
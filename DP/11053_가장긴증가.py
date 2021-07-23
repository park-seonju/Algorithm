n=int(input())
arr=list(map(int,input().split()))
dp=[0]*n
# 처음에는 dp[0]=1 / 
for i in range(n):
    temp=0
    for j in range(i):
        if arr[i] > arr[j]: # 가장 오른쪽 기준 / 0번부터 비교
            temp=max(temp,dp[j]) # 크다면 기존 dp에서 젤큰거 temp에 넣음
    dp[i]=temp+1 # 다 비교했으면 현재숫자까지 +1 해줌
print(max(dp))
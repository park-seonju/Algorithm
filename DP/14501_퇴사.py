n=int(input())
T=[0]*n
P=[0]*n
for i in range(n):
    time,price=map(int,input().split())
    T[i]=time
    P[i]=price
DP=[0]*n
 
if T[n-1]==1:  # 마지막이 하루면 DP 마지막에 금액미리넣어줌
    DP[n-1]=P[n-1]

for i in range(n-2,-1,-1): #뒤부터 반복
    day=i+T[i] #날짜 + 그날 일하는일수 = 총 일수
    if day==n:  # 마지막날이면 
        DP[i]=max(P[i],DP[i+1]) #그날에 보상 or 여태까지 일한거
    elif day<n: # 총 일수가 전체 날보다 작으면
        DP[i]=max(P[i]+DP[day],DP[i+1]) # 그날 보상+그날일할때넘어가는날까지의보상 or 여태까지 일한거
    elif day>n: # 총 일수가 전체 날보다 크면
        DP[i]=DP[i+1] # 다음날 껄 넣어줌
print(DP[0])
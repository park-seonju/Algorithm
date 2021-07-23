from itertools import product
n=int(input())
three=[0,1,2]
ans=0
for i in product(three,repeat=n):
    if i[0]!=0:
        if sum(i)%3==0:
            ans+=1
print(ans)


# DP 풀이
# def make_it(i, sum):
#     if i==n:
#         if sum%3 == 0:
#             return 1
#         return 0

#     if dp[i][sum] >= 0:
#         return dp[i][sum]

#     dp[i][sum] = 0

#     for num in range(3):
#         dp[i][sum] += make_it(i+1, sum+num)

#     return dp[i][sum]

# n = int(input())
# dp = [[-1 for _ in range(20)] for _ in range(n)]
# if n==1: print(0)
# else: print(make_it(1, 1) + make_it(1,2))
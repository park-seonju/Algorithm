import sys
input=sys.stdin.readline
t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    dp = [[0]*(m+1) for _ in range(n+1)]
    print(dp)
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1:
                dp[i][j] = j
            else:
                if i == j:
                    dp[i][j] = 1
                elif i < j:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    print(dp[n][m])


# from itertools import combinations
# t=int(input())
# n,m=map(int,input().split())
# m_list=[]
# ans=[]
# for i in range(m):
#     m_list.append(i)
# print(m_list)
# for i in combinations(m_list,n):
#     print(i)
#     ans.append((i))
# print(len(ans))
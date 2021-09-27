n=int(input())
population=[0]+list(map(int,input().split()))
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    m1,m2 = map(int,input().split())
    adj[m1].append(m2)
    adj[m2].append(m1)
visited=[0]*(n+1)
dp = [[0,population[i]] for i in range(n+1)]
def check(node):
    visited[node]=1
    for e in adj[node]:
        if not visited[e]:
            check(e)
            dp[node][1]+=dp[e][0]
            dp[node][0]+=max(dp[e][0],dp[e][1])
    print('dp',dp)
    print('node',node)
    
check(1)
print(max(dp[1][1],dp[1][0]))
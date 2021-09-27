n=int(input())
weight=[0]+list(map(int,input().split()))
adj=[[] for _ in range(n+1)]
dp=[[0,weight[i]] for i in range(n+1)]
for _ in range(n-1):
    n1,n2=map(int,input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)
visited=[0]*(n+1)
def dfs(node):
    global ans
    visited[node]=1
    for e in adj[node]:
        if not visited[e]:
            dfs(e)
            dp[node][1]+=dp[e][0]
            dp[node][0]+=max(dp[e][0],dp[e][1])
ans=[]
ans_visited=[1]*(n+1)
def check(node,before):
    ans_visited[node]=0
    if before==0: # 이전 포함
        for e in adj[node]:
            if ans_visited[e]:
                check(e,1) # 현재 포함 X
    else:
        if dp[node][0]<dp[node][1]:
            ans.append(node)
            for e in adj[node]:
                if ans_visited[e]:
                    check(e,0)
        else:
            for e in adj[node]:
                if ans_visited[e]:
                    check(e,1)
dfs(1)
print(max(dp[1][0],dp[1][1]))
check(1,1)
ans.sort()
print(*ans)
from collections import deque
n=int(input())
pp=list(map(int,input().split()))
adj=[[] for _ in range(n)]
for i in range(n):
    info=list(map(int,input().split()))
    for num in info[1:]:
            adj[i].append(num-1)
def bfs(g):
    q=deque()
    check=[False for _ in range(n)]
    q.append(g[0])
    check[g[0]]=True
    cnt,answer=1,0
    while q:
        temp=q.popleft()
        answer +=pp[temp]
        for i in adj[temp]:
            if i in g and not check[i]:
                check[i]=True
                cnt+=1
                q.append(i)
    if cnt == len(g):
        return answer
    else:
        return False
def dfs(s,k,e):
    global ans
    if s == e:
        g1,g2 = deque(),deque()
        for i in range(n):
            if visited[i]:
                g1.append(i)
            else:
                g2.append(i)
        ans1=bfs(g1)
        if not ans1:
            return
        ans2=bfs(g2)
        if not ans2:
            return
        ans = min(ans,abs(ans1-ans2))
        return
    for i in range(k,n):
        if not visited[i]:
            visited[i]=True
            dfs(s+1,i,e)
            visited[i]=False
ans = 999999999
for i in range(1,n//2+1):
    visited=[False for _ in range(n)]
    dfs(0,0,i)

print(-1 if ans==999999999 else ans)
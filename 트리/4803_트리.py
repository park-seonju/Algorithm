def bfs(n):
    isTree=True
    q=[n]
    while q:
        now=q.pop(0)
        if visited[now]:isTree=False
        visited[now]=1
        for e in adj[now]:
            if not visited[e]:
                q.append(e)
    return isTree
tc=1
while 1:
    n,m=map(int,input().split())
    if n==0 and m==0: break
    adj=[[] for _ in range(n+1)]
    for _ in range(m):
        s,e=map(int,input().split())
        adj[s].append(e)
        adj[e].append(s)
    cnt=0
    visited=[0 for _ in range(n+1)]
    for i in range(1,n+1):
        if visited[i]:continue
        if bfs(i):cnt+=1
    if cnt>1:print("Case {}: A forest of {} trees.".format(tc,cnt))
    elif cnt==1:print("Case {}: There is one tree.".format(tc))
    else: print('Case {}: No trees.'.format(tc))
    tc+=1
from collections import deque
N,M=map(int,input().split())
adj = [[] for _ in range(N+1)]
ans=[999999999,0]
for _ in range(M):
    A,B=map(int,input().split())
    adj[A].append(B)
    adj[B].append(A)

for i in range(1,N+1):
    total=[0]*(N+1)
    visited=[0]*(N+1)
    q=deque()
    q.append((i,0))
    visited[i]=1
    while q:
        friend,cnt=q.popleft()
        total[friend]=cnt
        for e in adj[friend]:
            if not visited[e]:
                visited[e]=1
                q.append((e,cnt+1))
    temp=0
    for j in range(1,N+1):
        temp+=total[j]
    if ans[0] > temp: ans[0]=temp; ans[1]=i;
    
print(ans[1])
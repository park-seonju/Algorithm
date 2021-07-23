from collections import deque
n,k=map(int,input().split())
visited=[0]*100001
q=deque()
q.append((n,0))

while q:
    current,cnt=q.popleft()
    if current==k:print(cnt);break
    
    if 2*current<=100000 and not visited[2*current]:
        visited[2*current]=1
        q.append((current*2,cnt))
    if current-1>=0 and not visited[current-1]:
        visited[current-1]=1
        q.append((current-1,cnt+1))
    if current+1<=100000 and not visited[current+1]:    
        visited[current+1]=1
        q.append((current+1,cnt+1))
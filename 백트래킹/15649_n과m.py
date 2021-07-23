n,m=map(int,input().split())
visited=[0]*n

def bt(idx,n,m):
    if idx==m:
        print(' '.join(map(str,ans)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i]=True
            ans.append(i+1)
            bt(idx+1,n,m)
            visited[i]=False
            ans.pop()

ans=[]
bt(0,n,m)
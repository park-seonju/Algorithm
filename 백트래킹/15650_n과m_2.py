n,m=map(int,input().split())
visited=[0]*n

def bt(depth,idx,n,m):
    if depth==m:
        print(' '.join(map(str,ans)))
        return
    for i in range(idx,n):
        if not visited[i]:
            visited[i]=True
            ans.append(i+1)
            bt(depth+1,idx+1,n,m)
            visited[i]=False
            ans.pop()

ans=[]
bt(0,0,n,m)
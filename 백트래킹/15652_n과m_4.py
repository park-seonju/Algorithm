n,m=map(int,input().split())

def func(n,m,cnt,idx):
    if cnt==m:
        print(*ans)
        return
    for i in range(idx,n+1):
        ans.append(i)
        func(n,m,cnt+1,i)
        ans.pop()
visited=[0]*(n+1)
ans=[]
func(n,m,0,1)
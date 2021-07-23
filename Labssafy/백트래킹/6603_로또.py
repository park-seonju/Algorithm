def dfs(n,idx):
    if n==6:
        for i in range(k):
            if visited[i]:
                print(S[i],end=" ")
        print()
        return
    for i in range(idx,k):
        visited[i]=1
        dfs(n+1,i+1)
        visited[i]=0


A=list(map(int,input().split()))
k=A[0]
S=A[1:]
visited=[0]*k
dfs(0,0)
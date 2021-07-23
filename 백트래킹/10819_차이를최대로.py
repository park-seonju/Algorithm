n=int(input())
A=list(map(int,input().split()))
ans=[]
temp=[]
visited=[0]*n
def func(depth):
    if depth==n:
        total=0
        for i in range(n-1):
            total+=abs(temp[i+1]-temp[i])
        ans.append(total)
    for i in range(n):
        if not visited[i]:
            temp.append(A[i])
            visited[i]=1
            func(depth+1)
            visited[i]=0
            temp.pop()
func(0)
print(max(ans))
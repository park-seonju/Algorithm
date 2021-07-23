def dfs(depth,idx):
    if depth==l:
        ans.append(''.join(map(str,temp)))
        return
    for i in range(idx,c):
        temp.append(arr[i])
        dfs(depth+1,i+1)
        temp.pop()
def password(check):
    for i in check:
        cons=0
        vow=0
        for j in i:
            if j in 'aeiou':
                cons+=1
            else:
                vow+=1
        if cons>=1 and vow>=2:
            print(i)
    return
l,c=map(int,input().split())
arr=list(input().split())
arr.sort()
temp=[]
ans=[]
dfs(0,0)
password(ans)
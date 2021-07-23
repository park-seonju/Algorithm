def dfs(idx, sum_num, check):
    global cnt
    if sum_num>n:
        return
    if n==sum_num:
        cnt+=1
        if cnt==k:
            print("".join(check)[:-1])
            exit(0)
    for i in range(1,4):
        check.append(str(i)+'+')
        dfs(idx+1,sum_num+i,check)
        check.pop()
cnt=0
n,k=map(int,input().split())
dfs(0,0,[])
print(-1)
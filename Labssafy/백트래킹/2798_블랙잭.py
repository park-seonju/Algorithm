n,m=map(int,input().split())
num_list=list(map(int,input().split()))
ans=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sum=num_list[i]+num_list[j]+num_list[k]
            if sum<=m:
                if ans<sum:
                    ans=sum
print(ans)

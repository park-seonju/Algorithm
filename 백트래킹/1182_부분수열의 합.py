n,s=map(int,input().split())
arr=list(map(int,input().split()))
ans=0
def func(idx,total):
    global ans
    if idx>=n:
        if s==total:
            ans+=1
        return
    else:
        func(idx+1,total+arr[idx])
        func(idx+1,total)
func(0,0)
if s==0:
    print(ans-1)
else:
    print(ans)
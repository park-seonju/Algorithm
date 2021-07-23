def go():
    t=False
    for i in range(len(op)):
        x,y=op[i][0],op[i][1]
        p,q=0,0
        if x<0:
            if sik[-x]==0:  # false 면 p를 true 로 바꿈 음수니까
                p=1
        else:
            p=sik[x]  # 양수니까 그냥 그대로 가져감
        if y<0:
            if sik[-y]==0:
                q=1
        else:
            q=sik[y]
        if not i:  
            t=(p|q)   # 처음식은 둘이 합
        else:           
            t=(t&(p|q)) # 나머진 그 전에꺼에 연산 
        if not t:
            return 0
    return 1
    
def func(a):
    if N+1 == a:
        if go(): return 1
        return 0
    sik[a]=1
    if(func(a+1)): return 1
    sik[a]=0
    if(func(a+1)): return 1

N,M=map(int,input().split())
sik=[-1]*21
op=[list(map(int,input().split())) for _ in range(M)]
if func(1):
    print(func(1))
else:
    print(0)

n,m = map(int,input().split())
adj = {}
for i in range(1,n+1):
    adj[i] = set()
    adj[-i] = set()
for i in range(m):
    a,b = map(int,input().split())
    adj[a].add(-b)
    adj[b].add(-a)
print(adj)
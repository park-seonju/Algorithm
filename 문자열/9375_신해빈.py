T=int(input())
for tc in range(T):
    n=int(input())
    dict1={}
    for _ in range(n):
        name,kinds=map(str,input().split())
        if kinds in dict1:
            # dict1[kinds].append(name)
            dict1[kinds]+=1
        else:
            dict1[kinds]=1
            # dict1[kinds]=[name]
    ans=1
    for key,value in dict1.items():
        ans*=value+1
    print(ans-1) # 아무것도 안 입을 때 빼기
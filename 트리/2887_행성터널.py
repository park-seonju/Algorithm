import sys
input=sys.stdin.readline

n=int(input())
info=[]
for idx in range(n):
    x,y,z=map(int,input().split())
    info.append((x,y,z,idx))
dist=[]
parents=[i for i in range(n+1)]

def find(x):
    if parents[x] != x:
        parents[x]=find(parents[x])
    return parents[x]

def union(x,y):
    root1=find(x) # 각노드의 그룹번호를 가져옴
    root2=find(y)
    parents[root2]=root1  # 보통 작은걸로 그룹의 넘버를 정함 if root1>root2 : parents[root1]=root2 근데 상관 x

def kruskal(n):
    cnt=0
    ans=0
    for val,s,e in dist:
        if find(s) != find(e): # 그룹이 다른상태면
            union(s,e) # 합쳐주기
            ans += val
            cnt+=1
        if cnt == n-1:break
    print(ans)

for i in range(3):
    info.sort(key=lambda x:x[i])
    for j in range(1,n):
        dist.append((abs(info[j][i]-info[j-1][i]),info[j][3],info[j-1][3]))

dist.sort()
kruskal(n)



# def find(x):
#     if parent[x]!=x:
#         parent[x]=find(parent[x])
#     return parent[x]

# def union(x,y):
#     root1=find(x)
#     root2=find(y)
#     parent[root2]=root1

# def kruskal(n):
#     ans=0
#     cnt=0
#     for w,a,b in info:
#         if find(a) != find(b):
#             cnt+=1
#             ans+=w
#             union(a,b)
#             if cnt==n-1:break
#     return ans
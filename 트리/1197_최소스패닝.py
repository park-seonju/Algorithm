def find(x):
    if parents[x]==x:
        return x
    else:
        y=find(parents[x])
        parents[x]=y
        return y

def union(x,y):
    root1=find(x)
    root2=find(y)
    if root1!=root2:
        parents[root2]=root1

V,E=map(int,input().split())
dist=[]
parents=[i for i in range(V+1)]

for _ in range(E):
    a,b,c=map(int,input().split())
    dist.append([c,a,b])
dist.sort(key=lambda x:x[0])

mst_cost=0
cnt=0
for val,s,e in dist:
    if find(s) != find(e):
        union(s,e)
        mst_cost += val
        cnt+=1
    if cnt==V-1:break   
print(mst_cost)
N=int(input())
node=list(map(int,input().split()))
cut=int(input())
# adj=[[] for _ in range(N)]
cnt=0
tree={x:[] for x in range(N)}
for i in range(N):
    if node[i] == -1:
        continue
    tree[node[i]].append(i)

q=[cut]
pop=[cut]

while q:
    next=q.pop()
    for i in tree[next]:
        q.append(i)
        pop.append(i)

for i in pop:
    del tree[i]
    for key,value in tree.items(): #자르는 노드를 갖고있는 부모노드 확인
        for v in value:  
            if i==v and len(value)==1: #i,v자르려는 노드 1개 있을때만 혼자있는 트리이므로
                tree[key]=[]

for value in tree.values():
    if value==[]:
        cnt+=1
print(cnt)
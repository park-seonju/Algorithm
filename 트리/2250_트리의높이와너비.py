n= int(input())
adj=[[] for _ in range(n+1)]
find_root = [0]*(n+1)
for _ in range(n):
    p,c1,c2 = map(int,input().split())
    adj[p].append(c1)
    adj[p].append(c2)
    find_root[p]+=1
    if c1 != -1:
        find_root[c1]+=1
    if c2 != -1:
        find_root[c2]+=1
root = 0
for i in range(1,n+1):
    if find_root[i]==1:
        root=i
num = 1
d=[[] for _ in range(n+1)] #깊이가 같은거 끼리 모아두는데 순서를 저장할 리스트
def inorder(start,deep):
    global num # 거리
    if adj[start][0] != -1:
        inorder(adj[start][0],deep+1)
    d[deep].append(num) #중위순회 할때 몇번째인지 수
    num+=1
    if adj[start][1] != -1:
        inorder(adj[start][1],deep+1)
inorder(root,1)
level = 1
ans = max(d[1])-min(d[1])+1
for i in range(2,n+1):
    if d[i]: # 그 깊이의 노드가 있다면
        temp = max(d[i])-min(d[i])+1
        if ans<temp: # 최대 차이가 나는 걸 ans 저장 깊이(level)랑
            ans = temp
            level=i
print(level)
print(ans)
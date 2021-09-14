import sys
input = sys.stdin.readline
k=int(input())
v=list(map(int,input().split()))
adj = [[] for _ in range(k)]
idx=0
def inorder(d):
    global adj,idx
    if d==k:
        return
    inorder(d+1)
    adj[d].append(v[idx])
    idx+=1
    inorder(d+1)
inorder(0)
for e in adj:
    print(*e)
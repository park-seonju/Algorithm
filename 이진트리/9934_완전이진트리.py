# import sys
# input = sys.stdin.readline
# k=int(input())
# v=list(map(int,input().split()))
# adj = [[] for _ in range(k)]
# idx=0
# def inorder(d):
#     global adj,idx
#     if d==k:
#         return
#     inorder(d+1)
#     adj[d].append(v[idx])
#     idx+=1
#     inorder(d+1)
# inorder(0)
# for e in adj:
#     print(*e)

import sys
input = sys.stdin.readline
k=int(input())
v=list(map(int,input().split()))
idx=0
adj = [[] for _ in range(k)]

def inorder(depth):
    global idx
    if depth==k:
        return
    inorder(depth+1)
    adj[depth].append(v[idx])
    idx+=1
    inorder(depth+1)

inorder(0)
for e in adj:
    print(*e)
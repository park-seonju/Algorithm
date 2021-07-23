import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
tree=[]
while 1:
    try:
        tree.append(int(input()))
    except:
        break

def postorder(tree,l,r):
    if l>r:return
    root=tree[l]
    left_start=l+1
    right_end=r
    right_start=r+1 # 루트보다 큰 자식이 없다면 빠져나와야하므로
    for i in range(1,r-l+1):
        if tree[l+i]>root:
            right_start=l+i
            break
    left_end=right_start-1
    postorder(tree,left_start,left_end)
    postorder(tree,right_start,right_end)
    answer.append(root)
answer=[]
postorder(tree,0,len(tree)-1)
for i in answer:
    print(i)

def postorder(v):
    if v == '.': return

    postorder(tree[v][0])
    postorder(tree[v][1])
    print(v, end='')

def preorder(v):
    if v == '.': return

    print(v, end='')
    preorder(tree[v][0])
    preorder(tree[v][1])

def inorder(v):
    if v == '.': return

    inorder(tree[v][0])
    print(v, end='')
    inorder(tree[v][1])

n=int(input())
# 배열로하면 메모리초과
tree={}
for _ in range(n):
    p,left,right=map(str,input().split())
    tree[p]=[left,right]

preorder('A')
print()
inorder('A')
print()
postorder('A')
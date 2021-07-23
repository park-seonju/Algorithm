n=int(input())
inOrder=list(map(int,input().split()))
postOrder=list(map(int,input().split()))

position = {}
for i in range(n):
    position[inOrder[i]] = i # 인오더에 인덱스가 나옴 숫자 넣어주면

def solve(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end: return
    root = postOrder[post_end]
    print(root, end=' ')
    p = position[root]
    left = p - in_start
    solve(in_start, p-1, post_start, post_start+left-1) #왼쪽
    solve(p+1, in_end, post_start+left, post_end-1) #오른쪽

solve(0, n-1, 0, n-1)
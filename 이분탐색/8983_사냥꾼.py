import sys
input = sys.stdin.readline
M,N,L = map(int,input().split())
xlist = list(map(int,input().split()))
animal = [list(map(int,input().split())) for _ in range(N)]
ans=set()
# 에니멀 x리스트 바꿔서 조건줘서 포문탈출
for cord in animal:
    a,b = cord
    if b>L: continue
    for x in xlist:
        if abs(x-a)+b <= L and x-L < a < x+L:
            ans.add((a,b))
print(len(ans))

# for x in xlist:
#     for cord in animal:
#         a,b = cord
#         if abs(x-a)+b <= L and b<=L and x-L < a < x+L:
#             ans.add((a,b))
# print(len(ans))
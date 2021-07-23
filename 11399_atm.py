# from itertools import permutations
# import sys
# input=sys.stdin.readline
# n=int(input())
# p=(map(int,input().split()))
# ans=99999999
# A=set()
# for i in permutations(p,n):
#     A.add(i)
# for i in A:
#     total=0
#     temp=0
#     for j in i:
#         total+=j
#         temp+=total
#     if temp<ans:ans=temp
# print(ans)

import sys
input=sys.stdin.readline
n=int(input())
p=list(map(int,input().split()))
p.sort()
ans=0
total=0
for i in p:
    total+=i
    ans+=total
print(ans)
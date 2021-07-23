# import sys
# from collections import deque
# input=sys.stdin.readline

# Test=int(input())
# num_list=[]
# abs_list=[]

# def check(num_list,abs_list):
#     i=abs_list.index(min(abs_list))  # num_list에서 최소 절대값 인덱스
#     if -num_list[i] in num_list:
#         print(-num_list[i])
#         num_list.remove(-num_list[i])
#     else:
#         print(num_list[i])
#         del num_list[i]
#     del abs_list[i]
#     return num_list

# for _ in range(Test):
#     num=int(input())
#     if num != 0 :
#         num_list.append(num)
#         abs_list.append(abs(num))
#     else:
#         if not num_list:
#             print(0)
#             continue
#         check(num_list,abs_list)

import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())

que = PriorityQueue()
ans = []
for _ in range(n):
    next = int(input())
    if next!=0:
        que.put((abs(next),next))
    elif not que.empty():
        ans.append(que.get()[1])
    else:
        ans.append(0)
print("\n".join(map(str, ans)))
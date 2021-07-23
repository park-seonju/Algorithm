# Test=int(input())
# for test in range(Test):
#     num=int(input())
#     cnt=0
#     num_list=list(map(int,input().split()))
#     for i in range(num-1,0,-1):
#         for j in range(0,i):
#             if num_list[j]>num_list[j+1]:
#                 cnt+=1
#                 num_list[j],num_list[j+1]=num_list[j+1],num_list[j]
#     print(num_list)
#     # for i in range(num-1):
#     #     for j in range(i,i+1):
#     #         if num_list[j]>num_list[j+1]:
#     #             cnt+=1
#     #             num_list[j],num_list[j+1]=num_list[j+1],num_list[j]
#     print("#{} {}".format(test+1,cnt))
# from collections import deque
# que=deque([[1,2],[1,3],[2,3]])
# # for i in range(len(que)):
# #     if i==0:
# #         que.remove(que[i])
# print(que.popleft()[0])
# list1=[1,2,3]
# list1[2]+1
# print(list1)
# a=(1,3)
# b=(4,5)
# a=b
# print(a)
a=[1,2,3,4]
b=""
c=a[0]+b
print(c)

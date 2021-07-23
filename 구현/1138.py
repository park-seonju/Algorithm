# num=int(input())
# left_look=list(map(int,input().split()))
# check_list=[]
# index=1
# for i in left_look:
#     check_list.append((i,index))
#     index+=1
# print(check_list)
# ans=[]
# for i in check_list:
#     if not ans: # 처음에 0 넣어줌
#         if i[0]==0:
#             ans.append(i[1])
#     elif len(ans)>=i[0]:
#         temp=(-1,11)
#         temp_list=[]
#         temp_list.append(i)
#         for j in temp_list:
#             if j[0]>=temp[0] and j[1]<temp[1]:
#                 temp=j
#         ans.append(temp[1])

# print(*ans)



N = int(input())
line = []
people = [-1] + list(map(int, input().split()))
print(people)
for n in range(N,0,-1):
    line.insert(people[n],n)
    print(line)
print(*line)




n = int(input())
h = list(map(int, input().split()))
ans = [0] * n
for p in range(1, n+1):
    t = h[p-1]
    cnt = 0
    for i in range(n):
        if cnt == t and ans[i] == 0:
            ans[i] = p
            break
        elif ans[i] == 0:
            cnt += 1
print(*ans)


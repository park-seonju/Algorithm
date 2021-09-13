from itertools import combinations
import sys
input = sys.stdin.readline
n = int(input())
nums = sorted(list(map(int,input().split())))
num = 99999999
# for x in combinations(nums,3):
#     temp = sum(x)
#     if abs(num) > abs(temp): #
#         num = temp
#         ans = sorted(list(x))
# print(*ans)

for i in range(n-2):
    s, e = i+1, n-1
    while s != e:
        total = nums[i] + nums[s] + nums[e]
        if abs(total) < num:
            num = abs(total)
            ans = [nums[i], nums[s], nums[e]]
        if total < 0: s+=1
        elif total > 0: e-=1
        else:
            print(nums[i], nums[s], nums[e])
            exit()
print(*ans)
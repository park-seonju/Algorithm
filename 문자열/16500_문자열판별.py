# import sys
# input=sys.stdin.readline
# s=input().rstrip()
# n=int(input())
# a=[input().rstrip() for _ in range(n)]
# temp=''
# start=0
# while temp!=s:
#     for i in a:
#         if i == s[start:start+len(i)]:
#             temp+=i
#             a.remove(i)
#             break
#     start+=len(temp)
# if s==temp:print(1)
# else:print(0)

# def solve(idx):
#     global ans
#     if idx==len(s):
#         ans=1
#         return
#     if dp[idx]:
#         return
#     dp[idx]=1
#     for i in range(len(a)):
#         if len(s[idx:])>=len(a[i]):
#             for j in range(len(a[i])):
#                 if a[i][j] != s[idx+j]: 
#                     break # 만나면 for문 나가고 i다시
#             else: # break가 발생하지 않았을때 실행
#                 solve(idx+len(a[i]))
#     return
# s=input().rstrip()
# n=int(input())
# a=[input().rstrip() for _ in range(n)]
# dp=[0]*101
# ans=0
# solve(0)
# print(ans)


def make_it(word):
    global possible
    if not word:
        possible = 1
        return
    index = len(s)-len(word)
    if dp[index]:
        return
    dp[index] = 1
    for i in range(n):
        if word.startswith(a[i]):
            make_it(word[len(a[i]):])

s = input().strip()
n = int(input())
a = []
for _ in range(n):
    a.append(input().strip())
dp = [0 for _ in range(len(s))]
possible = 0
make_it(s)
print(possible)


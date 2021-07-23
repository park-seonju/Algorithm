import sys
from collections import deque
input=sys.stdin.readline
total_num=int(input())
num=int(input())
que=deque()
ans=[]

for _ in range(num):
    que.append(list(map(int,input().split())))

for i in range(num):
    x,y=que.popleft()
    if x==1:
        ans.append(y)
    else:
        que.append([x,y])

ans_copy=list(ans)

for friend in ans_copy:
    for i in range(len(que)):
        x,y=que.popleft()
        if friend==x and y not in ans:
            ans.append(y)
        elif friend == y and x not in ans:
            ans.append(x)
        que.append([x,y])
print(len(ans))
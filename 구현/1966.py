import sys
from collections import deque
input=sys.stdin.readline
Test=int(input())
ans=[]
while Test>0:
    Test-=1
    N,M=map(int,input().split())
    que=list(map(int,input().split()))
    list1=[]
    for i in range(N):
        list1.append(que[i])
    # list1=que X
    cnt=0
    same=0
    for _ in range(N):
        if len(list1)==1:
            cnt+=1
            break
        one=que.pop()
        if list1[M]<=one:
            cnt+=1
            if list1[M]==one:
                same+=1
    ans.append(cnt)
    # 같은 수 처리 어떻게..?
    if same>=2:
        ans.pop()
        ans.append(same)

for i in ans:
    print(i)






num = int(input())
for _ in range(num):
    N, M = map(int,input().split())
    que = deque(map(int,input().split()))
    cnt = 0
    while que:
        top = max(que)
        pop = que.popleft()
        M -= 1 # 인덱스 밀어주기  M = index     3 4 1 2  =>  2
        if top != pop:
            que.append(pop)
            if M < 0:  # 음수 인덱스는 없으므로 다시 길이-1 만큼으로 초기화
                M = len(que)-1
        else: #최대면
            cnt+=1 # 최대가 우선이니 카운트
            if M == -1:  # 한바퀴 다 돌거나 맨 왼쪽에 있던 것 이므로
                print(cnt)
                break
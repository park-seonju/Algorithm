n,h=map(int,input().split())
bottom=[]
top=[]
# for _ in range(n//2):
#     bottom.append(int(input()))
#     top.append(int(input()))
# 뭘 기준으로 탐색을 해야할지 모르겠음

# 종유석은 h-arr[idx] < h: cnt+=1
# b_max=max(bottom)
# t_max=max(top)
# b_cnt=0
# t_cnt=0
# for i in bottom:
#     if h-t_max < i:b_cnt+=1
# for j in top:
#     if h-b_max < j:t_cnt+=1
# if b_cnt>t_cnt:
#     print(t_max)



arr = [int(input()) for _ in range(n)]
up = [0] * (h+2)
down = [0] * (h+2)
result = [0] * (h+2)

for i in range(n):
    height=arr[i]
    if i%2:
        up[h-height]+=1
    else:
        down[height+1] +=1

for i in range(2,h+1):
    down[i]+=down[i-1]

for i in range(h,-1,-1):
    up[i]+=up[i+1]

for i in range(1,h+1):
    result[i] = up[i]+down[i]

print(n-max(result),result.count(max(result)))


import sys

input = sys.stdin.readline

n, height = map(int, input().split())

col = [int(input()) for _ in range(n)]
a = col[0:n:2]
b = col[1:n:2]

a.sort()
b.sort(reverse=True)

cnt = len(a)
i, j = 0, 0
ans = n
ansCnt = 1
for h in range(1, height+1):

    while i<len(a):
        if a[i] < h:
            cnt -= 1
            i += 1
        else: break

    h = height-h
    while j<len(b):
        if b[j] > h:
            cnt += 1
            j += 1
        else: break
        
    if ans < cnt: continue
    elif ans == cnt:
        ansCnt += 1
    else:
        ans = cnt
        ansCnt = 1
print(ans, ansCnt)
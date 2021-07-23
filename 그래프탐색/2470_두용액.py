import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
# 배열 값 말고 index로 선언이 쉬움
s=0
e=n-1
temp=sys.maxsize
while s<e:
    mix = arr[s]+arr[e]
    # 절대값이 가장 작은게 0에 가까운것
    if abs(mix)<temp:
        ans=[arr[s],arr[e]]
        temp=abs(mix)
    if mix>=0:
        e-=1
    else:
        s+=1
print(*ans)
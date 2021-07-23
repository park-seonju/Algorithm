import sys
input=sys.stdin.readline
N=int(input())
people=[]
## 못품.
for _ in range(N):
    weight,height=map(int,input().split())
    people.append((weight,height))

for one in people:
    rank=1
    for two in people:
        if(one[0]!=two[0])&(one[1]!=two[1]):   # 첫번째 경우 제외
            if(one[0]<two[0])&(one[1]<two[1]):   # 클 경우만 랭크세주면 됨
                rank+=1
    print(rank,end=' ')
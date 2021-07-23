import sys
input=sys.stdin.readline
Test=int(input())
total=[]
for _ in range(Test):
    total.append(int(input()))

total.sort()   # 처음에 sort안해주면 최빈값 찾기 힘듬

print(round(sum(total)/len(total)))

print(total[len(total)//2])

cnt={}

for i in total:
    if i in cnt:
        cnt[i]+=1
    else:
        cnt[i]=1

cnt=sorted(cnt.items(),key=lambda x:x[1],reverse=True)

if (len(cnt) != 1) :
    if cnt[0][1] == cnt[1][1]: #같으면 00 10 같으니까
        print(cnt[1][0])
    else: # 다르면 첫번째
        print(cnt[0][0])
else:
    print(cnt[0][0])


print(max(total)-min(total))
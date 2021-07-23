import sys
input=sys.stdin.readline
Test=int(input())
for test_num in range(Test):
    impossible=False
    bbang_list=[0]*101
    people_sec_cnt=list(map(int,input().split()))
    when_come=list(map(int,input().split()))
    cnt=0
    for i in range(people_sec_cnt[1],101,people_sec_cnt[1]):
        bbang_list[i]+=people_sec_cnt[2]
    for i in when_come:
        for j in range(i,-1,-1):
            if bbang_list[j]>0:
                bbang_list[j]-=1
                break
            else:
                cnt+=1
        if i+1==cnt:
            impossible=True #impossible
            break
        cnt=0
    if impossible:
        print("#{} Impossible".format(test_num+1))
    else:
        print("#{} Possible".format(test_num+1))
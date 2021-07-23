import sys
input=sys.stdin.readline
num,th=list(map(int,input().split()))

def func(num_list):
    if len(num_list)==0:
        return 0
    minimum=min(num_list)
    for i in range(minimum,num+1,minimum):
        temp=set(num_list)
        temp.discard(i)
        if i not in check_list:
            check_list.append(i)
        num_list=list(sorted(temp))
    func(num_list)

num_list=[]
check_list=[]

for i in range(2,num+1):
    num_list.append(i)

func(num_list)

print(check_list[th-1])
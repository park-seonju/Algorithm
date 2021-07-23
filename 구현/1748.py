import sys
input=sys.stdin.readline

num=int(input().rstrip())
cnt=0
# for i in range(1,num+1):
#     cnt+=str(i)
# print(len(ans))

ans=0
length=len(str(num))
for i in range(1,length):
    ans+=i*(pow(10,i)-pow(10,i-1))
ans+=length*(num-pow(10,length-1)+1)
print(ans)

# 1~9 =>1  10-1개 1 
# 10~ 99=>2  100-10 2
# 100~999 -> 3  1000-100 3

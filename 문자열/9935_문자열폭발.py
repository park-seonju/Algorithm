# import sys
# input=sys.stdin.readline
# string=input().rstrip()
# bomb=input().rstrip()
# L=len(bomb)
# idx=0
# if len(string)<L:
#     print(string)
#     exit()
# while 1:
#     if string[idx:idx+L] == bomb:
#         string = string[:idx]+string[idx+L:]
#         idx-=2
#     idx+=1
#     if idx==len(string)-1:break
#     if idx<0:idx=0
# if not string:
#     print('FRULA')
# else:
#     print(string)


string=input()
bomb=input()

ans=[]

for i in string:
    ans.append(i)
    print(ans)
    if len(ans)>=len(bomb):
        check=[]
        checkcnt=0
        flag=True
        for j in range(-1,(-len(bomb)-1),-1):
            print(ans[j],bomb[j])
            if ans[j] != bomb[j]:
                flag=False
                break
        if flag:
            a=0
            while a<len(bomb):
                ans.pop()
                a+=1
if not ans:
    print("FRULA")
else:
    print("".join(ans))


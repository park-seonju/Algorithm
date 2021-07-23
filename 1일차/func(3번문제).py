def problem():
    num=int(input())
    n=0
    for i in range(2,num):
        if(num%i!=0):
           n+=1
    if(n==num-2):
        print('소수입니다.')
    else:
        print('소수가 아닙니다.')
problem() 
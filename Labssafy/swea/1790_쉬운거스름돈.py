T=int(input())
for tc in range(1,T+1):
    n=int(input())
    ans=[]
    money_list=[50000,10000,5000,1000,500,100,50,10]
    for money in money_list:
        ans.append(n//money)
        n%=money
    print('#{}'.format(tc))
    print(*ans)
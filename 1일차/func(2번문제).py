username1=input()
username2=input()
man1=input()
man2=input()
def rule(Man1,Man2):
    list1=["가위", "바위", "보"]
    for i in list1:
        if(Man1==i and Man2==i):
            print('비겼습니다!')
    if(Man1=='가위' and Man2=='바위'):
        print('바위가 이겼습니다!')
    if(Man1=='가위' and Man2=='보'):
        print('가위가 이겼습니다!')   
    if(Man1=='바위' and Man2=='가위'):
        print('바위가 이겼습니다!')
    if(Man1=='바위' and Man2=='보'):
        print('보가 이겼습니다!')  
    if(Man1=='보' and Man2=='가위'):
        print('가위가 이겼습니다!')
    if(Man1=='보' and Man2=='바위'):
        print('보가 이겼습니다!')  
rule(man1,man2)
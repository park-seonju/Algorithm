list1=["가위", "바위", "보"]
Man1=input()
Man2=input()
for i in list1:
    if(Man1==i and Man2==i):
        print('Result : Draw')
if(Man1=='가위' and Man2=='바위'):
    print('Result : Man2 Win!')
if(Man1=='가위' and Man2=='보'):
    print('Result : Man1 Win!')   
if(Man1=='바위' and Man2=='가위'):
    print('Result : Man1 Win!')
if(Man1=='바위' and Man2=='보'):
    print('Result : Man2 Win!')  
if(Man1=='보' and Man2=='가위'):
    print('Result : Man2 Win!')
if(Man1=='보' and Man2=='바위'):
    print('Result : Man1 Win!')  
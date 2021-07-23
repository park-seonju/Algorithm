list1=["가위", "바위", "보"]
Man1=input()
Man2=input()
if(Man1==list1[0] and Man2==list1[0]):
    print('Result : Draw')
if(Man1==list1[0] and Man2==list1[1]):
    print('Result : Man2 Win!')
if(Man1==list1[0] and Man2==list1[2]):
    print('Result : Man1 Win!')
if(Man1==list1[1] and Man2==list1[0]):
    print('Result : Man1 Win!')
if(Man1==list1[1] and Man2==list1[1]):
    print('Result : Draw')
if(Man1==list1[1] and Man2==list1[2]):
    print('Result : Man2 Win!')
if(Man1==list1[2] and Man2==list1[0]):
    print('Result : Man1 Win!')
if(Man1==list1[2] and Man2==list1[1]):
    print('Result : Man2 Win!')
if(Man1==list1[2] and Man2==list1[2]):
    print('Result : Draw')
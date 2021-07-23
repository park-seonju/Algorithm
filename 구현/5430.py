import sys
from collections import deque
input=sys.stdin.readline

def AC(array,num):
    flag=-1
    for i in order:
        if i == 'R':
            flag*=-1
        elif i== 'D':
            if not array or num == 0:
                return 'error'
            if flag == -1 :
                array.popleft()
            elif flag == 1:
                array.pop()
    if flag == -1:
        return array
    elif flag == 1:
        array.reverse()
        return array
    
Test=int(input())
for _ in range(Test):
    order=input().strip()
    num=int(input())
    array=deque(input().strip()[1:-1].split(','))
    array=AC(array,num)
    if array=='error':
        print('error')
    else:
        print('[',end='')
        for i in range(len(array)):
            if i == len(array)-1:
                print(str(array[i]),end='')
            else:
                print(array[i],end=',')
        else:
            print("]")

import sys
from collections import deque
input=sys.stdin.readline

def plus(deque_list):
    temp=deque_list.pop()
    deque_list.insert(0,temp)
    return deque_list

def minus(deque_list):
    temp=deque_list.popleft()
    deque_list.append(temp)
    return deque_list

t1=deque(list(map(int,input().strip())))
t2=deque(list(map(int,input().strip())))
t3=deque(list(map(int,input().strip())))
t4=deque(list(map(int,input().strip())))

cnt=int(input())
rotate=[]
for _ in range(cnt):
    rotate.append(list(map(int,input().split())))


for i in rotate:
    if i[0]==1:
        if t1[2]!=t2[6]:
            if t2[2]!=t3[6]:
                if t3[2]!=t4[6]:
                    if i[1]==1:
                        t1=plus(t1)
                        t2=minus(t2)
                        t3=plus(t3)
                        t4=minus(t4)
                    else:
                        t1=minus(t1)
                        t2=plus(t2)
                        t3=minus(t3)
                        t4=plus(t4)
                else:
                    if i[1]==1:
                        t1=plus(t1)
                        t2=minus(t2)
                        t3=plus(t3)
                    else:
                        t1=minus(t1)
                        t2=plus(t2)
                        t3=minus(t3)
            else:
                if i[1]==1:
                    t1=plus(t1)
                    t2=minus(t2)
                else:
                    t1=minus(t1)
                    t2=plus(t2)
        else:
            if i[1]==1:
                t1=plus(t1)
            else:
                t1=minus(t1)
    elif i[0]==2:
        if t2[6]!=t1[2] and t2[2]!=t3[6]:
            if t3[2]!=t4[6]:
                if i[1]==1:
                    t1=minus(t1)
                    t2=plus(t2)
                    t3=minus(t3)
                    t4=plus(t4)
                else:
                    t1=plus(t1)
                    t2=minus(t2)
                    t3=plus(t3)
                    t4=minus(t4)
            else:
                if i[1]==1:
                    t1=minus(t1)
                    t2=plus(t2)
                    t3=minus(t3)
                else:
                    t1=plus(t1)
                    t2=minus(t2)
                    t3=plus(t3) 
        elif t2[6]==t1[2] and t2[2]!=t3[6]:
            if t3[2]!=t4[6]:
                if i[1]==1:
                    t2=plus(t2)
                    t3=minus(t3)
                    t4=plus(t4)
                else:
                    t2=minus(t2)
                    t3=plus(t3)
                    t4=minus(t4)
            else:
                if i[1]==1:
                    t2=plus(t2)
                    t3=minus(t3)
                else:
                    t2=minus(t2)
                    t3=plus(t3)
        elif t2[6]!=t1[2] and t2[2]==t3[6]:
            if i[1]==1:
                t2=plus(t2)
                t1=minus(t1)
            else:
                t2=minus(t2)
                t1=plus(t1)
        else:
            if i[1]==1:
                t2=plus(t2)
            else:
                t2=minus(t2)
    elif i[0]==3:
        if t3[2]!=t4[6] and t3[6]!=t2[2]:
            if t2[6]!=t1[2]:
                if i[1]==1:
                    t1=plus(t1)
                    t2=minus(t2)
                    t3=plus(t3)
                    t4=minus(t4)
                else:
                    t1=minus(t1)
                    t2=plus(t2)
                    t3=minus(t3)
                    t4=plus(t4)
            else:
                if i[1]==1:
                    t2=minus(t2)
                    t3=plus(t3)
                    t4=minus(t4)
                else:
                    t2=plus(t2)
                    t3=minus(t3) 
                    t4=plus(t4)
        elif t3[2]==t4[6] and t3[6]!=t2[2]:
            if t2[6]!=t1[2]:
                if i[1]==1:
                    t1=plus(t1)
                    t2=minus(t2)
                    t3=plus(t3)
                else:
                    t1=minus(t1)
                    t2=plus(t2)
                    t3=minus(t3)
            else:
                if i[1]==1:
                    t2=minus(t2)
                    t3=plus(t3)
                else:
                    t2=plus(t2)
                    t3=minus(t3)
        elif t3[2]!=t4[6] and t3[6]==t2[2]:
            if i[1]==1:
                t3=plus(t3)
                t4=minus(t4)
            else:
                t3=minus(t3)
                t4=plus(t4)
        else:
            if i[1]==1:
                t3=plus(t3)
            else:
                t3=minus(t3) 
    elif i[0]==4:
        if t4[6]!=t3[2]:
            if t3[6]!=t2[2]:
                if t2[6]!=t1[2]:
                    if i[1]==1:
                        t4=plus(t4)
                        t3=minus(t3)
                        t2=plus(t2)
                        t1=minus(t1)
                    else:
                        t4=minus(t4)
                        t3=plus(t3)
                        t2=minus(t2)
                        t1=plus(t1)
                else:
                    if i[1]==1:
                        t4=plus(t4)
                        t3=minus(t3)
                        t2=plus(t2)
                    else:
                        t4=minus(t4)
                        t3=plus(t3)
                        t2=minus(t2)
            else:
                if i[1]==1:
                    t4=plus(t4)
                    t3=minus(t3)
                else:
                    t4=minus(t4)
                    t3=plus(t3)
        else:
            if i[1]==1:
                t4=plus(t4)
            else:
                t4=minus(t4)
print(t1[0]+(2*t2[0])+(4*t3[0])+(8*t4[0]))
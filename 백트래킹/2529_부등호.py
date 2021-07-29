import sys
input=sys.stdin.readline
k=int(input())
op=list(input().split())
Min=[]
Max=[]
def findMax(num_list,depth,num):
    global Max
    if depth==k:
        Max=num_list
        return
    for i in range(9,-1,-1):
        if not Max:
            if i not in num_list:
                if op[depth]=='<' and num<i:
                    findMax(num_list+[i],depth+1,i)
                if op[depth]=='>' and num>i:
                    findMax(num_list+[i],depth+1,i)

def findMin(num_list,depth,num):
    global Min
    if depth==k:
        Min=num_list
        return
    for i in range(10):
        if not Min:
            if i not in num_list:
                if op[depth]=='<' and num<i:
                    findMin(num_list+[i],depth+1,i)
                if op[depth]=='>' and num>i:
                    findMin(num_list+[i],depth+1,i)

for s in range(9,-1,-1):
    findMax([s],0,s)    

for s in range(10):
    findMin([s],0,s)

print(''.join(map(str,Max)))
print(''.join(map(str,Min)))
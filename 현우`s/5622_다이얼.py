import sys
input=sys.stdin.readline
words=input().strip()
ans=0
for word in words:
    if word=='A' or word=='B' or word=='C': ans+=3
    elif word=='D' or word=='E' or word=='F': ans+=4
    elif word=='G' or word=='H' or word=='I': ans+=5
    elif word=='J' or word=='K' or word=='L': ans+=6
    elif word=='O' or word=='M' or word=='N': ans+=7
    elif word=='R' or word=='Q' or word=='P' or word=='S': ans+=8
    elif word=='T' or word=='U' or word=='V': ans+=9
    elif word=='Z' or word=='Y' or word=='W' or word =='X': ans+=10
print(ans)
n=int(input())
index=1
for i in range(1,n+1):
    if n==1:
        print('*')
        break
    if i==1:
        print('*'*(4*n-3))
    elif i<3:
        print('* '*(i-1)+'*'*((n*4)-(i*4-3)))
    else:
        print('* '*(i-1)+'*'*((n*4)-(i*4-3))+' *'*index)
        index+=1
    if i==1:
        print('*')
    elif i==n:
        print('*'+' *'*(n*2-2))
    else:
        print('* '*i+' '*((n-i)*4-1)+' *'*(i-1))
if n!=1:
    print('*'+' *'*(n*2-2))
for i in range(n-1,0,-1):
    print('* '*i+' '*((n-i)*4-3)+' *'*i)
    print('* '*(i-1)+'*'*((n-i)*4+1)+' *'*(i-1))

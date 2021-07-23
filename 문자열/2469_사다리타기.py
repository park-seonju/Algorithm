import sys
input=sys.stdin.readline

k=int(input())
n=int(input())
s=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:k])
e=list(input().rstrip())
a=[input() for _ in range(n)]
for m in range(n): # 행 부분
    if a[m][0]=='?':  #사다리 처음이 ? 면 끗
        break
    for j in range(k-1): #열 부분
        if a[m][j]=='-':
            s[j],s[j+1]=s[j+1],s[j] # 열의 해당하는 알파벳 오른쪽으로 !!
print(m)
for i in range(n-1,m,-1):
    for j in range(k-1):
        if a[i][j]=='-':
            e[j],e[j+1]=e[j+1],e[j]
print('start',s)
print('end  ',e)
ans=''
for i in range(k-1):
    if s[i]==e[i+1] and s[i+1]==e[i]:
        ans+='-'
    else:
        ans+='*'
for i in range(k-1):
    if ans[i]=='-':
        s[i],s[i+1]=s[i+1],s[i]
if s==e:
    print(ans)
else:
    print('x'*(k-1))
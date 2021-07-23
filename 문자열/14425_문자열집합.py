import sys
input=sys.stdin.readline
n,m=map(int,input().split())
S={}

for _ in range(n):
    word=input()
    S[word]=True

cnt=0
for _ in range(m):
    word=input()
    if word in S.keys():
        cnt+=1
print(cnt)
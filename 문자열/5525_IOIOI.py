import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
S=input().strip()
cnt=0
k=1
ans=0
while k<m-1:
    if S[k-1]=='I' and S[k]=='O' and S[k+1]=='I' :
        k+=1 # index 두칸씩 넘어가야하니까
        cnt+=1 # IOI묶음카운트
        if cnt==n: # 그 묶음이면
            ans+=1 # 답올려주고
            cnt-=1 # 묶음 하나 빼주고
    else:
        cnt=0
    k+=1
print(ans)
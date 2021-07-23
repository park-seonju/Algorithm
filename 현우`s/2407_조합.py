n,m=map(int,input().split())
cnt=0
top=1
while cnt<m:
    cnt+=1
    top*=n
    n-=1

for i in range(m,1,-1):
    top//=i
print(top)

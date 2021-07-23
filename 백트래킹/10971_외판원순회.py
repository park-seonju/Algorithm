import sys
input=sys.stdin.readline
n=int(input())
W=[list(map(int,input().split())) for _ in range(n)]
visited=[0]*n
ans=999999999
def func(row,total):
    global ans
    if total<ans:
        if all(visited) and row==0:
            ans=min(ans,total)
        for i in range(n):
            if W[row][i] and not visited[i]:
                visited[i]=1
                func(i,total+W[row][i])
                visited[i]=0
func(0,0)
print(ans)

import sys
input=sys.stdin.readline
n=int(input())
W=[list(map(int,input().split())) for _ in range(n)]
row=[0]*n
column=[0]*n
ans=999999999
temp=[]
def func(r,c):
    global ans
    if len(temp)==n:
        ans=min(ans,sum(temp))
        return
    for i in range(n):
        if not row[i]:
            for j in range(n):
                if not column[j] and W[i][j]:
                    column[j]=1
                    row[i]=1
                    temp.append(W[i][j])
                    func(i,j)
                    temp.pop()
                    column[j]=0
                    row[i]=0
func(0,0)
print(ans)


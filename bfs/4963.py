import sys
input = sys.stdin.readline



ans = []
def dfs(y,x):
    dx=[1,-1,0,0,1,-1,-1,1]
    dy=[0,0,-1,1,1,1,-1,-1]
    visited[y][x]=1
    for k in range(8):
        NextR=y+dy[k]
        NextC=x+dx[k]
        if 0<=NextR<h and 0<=NextC<w:  # wow 변수이름 겹침
            if visited[NextR][NextC]==0 and board[NextR][NextC] == 1:
                print('도냐?')
                dfs(NextR,NextC)


while (1):
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    board=[]
    for _ in range(h):
        board.append(list(map(int,input().split())))
    visited=[[0]*w for _ in range(h)]
    cnt=0
    for i in range(h):
        for j in range(w):
            if visited[i][j]==0 and board[i][j]==1:
                dfs(i,j)
                cnt+=1
    ans.append(cnt)
    
for m in range(len(ans)):
    print(ans[m],end=' ')
# print("\n".join(map(str,ans)))  # join 이 string만 사용가능
#0    01   =>2       111                1
# 1   10            111   =>6
# 1
# 3
# 1
# 9
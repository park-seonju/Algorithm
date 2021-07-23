dx=[0,0,-1,1]
dy=[-1,1,0,0]
def DP(start,cnt):
    global ans
    i = start[0];j=start[1]
    print(cnt,i,j)
    print(dp)
    if dp[i][j] < cnt:return
    if i==e[0] and j==e[1]: ans=cnt
    for _ in range(4):
        nx = i + dx[_]
        ny = j + dy[_]
        if 0<=nx<4 and 0<=ny<5 and board[nx][ny]=='_':
            if dp[nx][ny] > cnt:
                dp[nx][ny] = cnt
                DP([nx,ny],cnt+1)
    

board=[list(map(str,input())) for _ in range(4)]

s=[0,0]
e=[0,0]
for i in range(4):
    for j in range(5):
        if board[i][j]=='A':s=[i,j]
        elif board[i][j]=='B':e=[i,j]
dp=[[21]*5 for _ in range(4)]
ans=1
DP(s,ans)
print(dp)
print(ans)
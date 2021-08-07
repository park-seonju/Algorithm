import sys
input=sys.stdin.readline
n,m,r=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
R=list(map(int,input().split()))
rotate=[[] for _ in range(m)]
first=True
for op in R:
    if op==1:
        for i in range(n//2):
            board[i],board[n-1-i]=board[n-1-i],board[i]
    elif op==2:
        for i in range(n):
            for j in range(m//2):
                board[i][j],board[i][m-1-j]=board[i][m-1-j],board[i][j]
    elif op==3:
        if first:
            for j in range(m):
                for i in range(n-1,-1,-1):
                    rotate[j].append(board[i][j])
            board=rotate
            rotate=[[] for _ in range(m)]
            first=False
        else:
            for j in range(n):
                for i in range(m-1,-1,-1):
                    rotate[j].append(board[i][j])
            board=rotate
            rotate=[[] for _ in range(n)]
            first=True
    elif op==4:
        if first:
            idx=0
            for j in range(m-1,-1,-1):
                for i in range(n):
                    rotate[idx].append(board[i][j])
                idx+=1
            board=rotate
            rotate=[[] for _ in range(m)]
            first=False
        else:
            idx=0
            for j in range(n-1,-1,-1):
                for i in range(m):
                    rotate[idx].append(board[i][j])
                idx+=1
            board=rotate
            rotate=[[] for _ in range(n)]
            first=True
    elif op==5:
        for i in range(n//2):
            for j in range(m//2):
                board[i][j],board[i][m//2+j]=board[i][m//2+j],board[i][j]
        for i in range(n//2):
            for j in range(m//2):
                board[i][j],board[n//2+i][m//2+j]=board[n//2+i][m//2+j],board[i][j]
        for j in range(m//2):
            for i in range(n//2):
                board[i][j],board[n//2+i][j]=board[n//2+i][j],board[i][j]
    elif op==6:
        for j in range(m//2):
            for i in range(n//2):
                board[i][j],board[n//2+i][j]=board[n//2+i][j],board[i][j]
        for i in range(n//2):
            for j in range(m//2):
                board[i][j],board[n//2+i][m//2+j]=board[n//2+i][m//2+j],board[i][j]
        for i in range(n//2):
            for j in range(m//2):
                board[i][j],board[i][m//2+j]=board[i][m//2+j],board[i][j]

# 마지막 출력
for i in range(len(board)):
    print(*board[i])
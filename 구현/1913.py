num=int(input())
K=int(input())
board=[[0]*num for _ in range(num)]
dr=[0,1,0,-1]
dc=[1,0,-1,0]
cnt=num**2
board[0][0]=cnt
nr,nc=0,0
row_col=[]
if cnt==K:
    row_col.append([nc+1,nr+1])
for _ in range(2*num-1): #7번 -> 밑 왼 위 0 1 2 3 
    if _%4 == 0:
        nr=nr+dr[0]
        nc=nc+dc[0]
        while 0<=nr<num and 0<=nc<num and board[nc][nr]==0:
            cnt-=1
            if cnt==K:
                row_col.append([nc+1,nr+1])
            board[nc][nr]=cnt
            nr,nc=nr+dr[0],nc+dc[0]
        nr-=dr[0]
        nc-=dc[0]
    elif _%4 == 1:
        nr=nr+dr[1]
        nc=nc+dc[1]
        while 0<=nr<num and 0<=nc<num and board[nc][nr]==0:
            cnt-=1
            if cnt==K:
                row_col.append([nc+1,nr+1])
            board[nc][nr]=cnt
            nr,nc=nr+dr[1],nc+dc[1]
        nr-=dr[1]
        nc-=dc[1]
    elif _%4 == 2:
        nr=nr+dr[2]
        nc=nc+dc[2]
        while 0<=nr<num and 0<=nc<num and board[nc][nr]==0:
            cnt-=1
            if cnt==K:
                row_col.append([nc+1,nr+1])
            board[nc][nr]=cnt
            nr,nc=nr+dr[2],nc+dc[2]
        nr-=dr[2]
        nc-=dc[2]
    elif _%4 == 3:
        nr=nr+dr[3]
        nc=nc+dc[3]
        while 0<=nr<num and 0<=nc<num and board[nc][nr]==0:
            cnt-=1
            if cnt==K:
                row_col.append([nc+1,nr+1])
            board[nc][nr]=cnt
            nr,nc=nr+dr[3],nc+dc[3]
        nr-=dr[3]
        nc-=dc[3]
for i in board:
    print(*i)
for i in row_col:
    print(*i)
def BINGO(bingo):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    cx=[-1,1,-1,1]
    cy=[1,-1,-1,1]
    what=0
    check_list=[[0,0],[1,1],[2,2],[3,3],[4,4]]
    for i in check_list:
        if bingo[i[0]][i[1]] != 0:
            continue
        cnt = 0
        if i==[2,2]:
            for _ in range(4):
                nx = 2 + cx[_]
                ny = 2 + cy[_]
                while 0<=nx<5 and 0<=ny<5:
                    if bingo[nx][ny]==0:
                        cnt+=1
                        nx+=cx[_]
                        ny+=cy[_]
                    else:
                        cnt=0
                        break
                if cnt==4:
                    what+=1
                    cnt=0
                    if what == 3:
                        return what
            cnt=0
        cnt=0
        for _ in range(4):
            nx = i[0] + dx[_]
            ny = i[1] + dy[_]
            while 0<=nx<5 and 0<=ny<5:
                if bingo[nx][ny]==0:
                    cnt+=1
                    nx+=dx[_]
                    ny+=dy[_]
                else:
                    cnt=0
                    break
            if cnt==4:
                what+=1
                cnt=0
                if what == 3:
                    return what
    return what
bingo=[]
for _ in range(5):
    bingo.append(list(map(int,input().split())))
check=[]
for _ in range(5):
    check.append(list(map(int,input().split())))

cnt=0
minimum=0
flag=False
for check_row in check:
    for num in check_row:
        cnt += 1
        for i in range(5):
            for j in range(5):
                if bingo[i][j]==num:
                    bingo[i][j]=0
                    minimum+=1
                else:
                    continue
                if minimum>=13:
                    ans=BINGO(bingo)
                    if ans >= 3:
                        print(cnt)
                        exit()
board=[]
for _ in range(19):
    board.append(list(map(int,input().split())))
def boundary(x, y):
    if x < 19 and x >= 0 and y < 19 and y >= 0:
        return True
    return False
dx = [0, 1, 1, 1]   # 하 우 오른아래대각 오른위대각
dy = [1, 0, 1, -1]
ans=[]
flag=False
for i in range(19):
    for j in range(19):
        if board[i][j]:
            for _ in range(4):
                ny=i
                nx=j
                cnt=1
                # if nx+dx[_]<19 and 0<=ny+dy[_]<19:
                    # while board[ny+dy[_]][nx+dx[_]]==board[ny][nx]:
                    #     cnt+=1
                    #     nx+=dx[_]
                    #     ny+=dy[_]
                    #     print('nx',nx,'ny',ny)
                    #     print('dx',dx[_],'dy',dy[_])
                    #     if (nx+dx[_])<19 and 0<(ny+dy[_])<19:
                    #         break
                while boundary(nx+dx[_],ny+dy[_])and board[ny][nx]==board[ny+dy[_]][nx+dx[_]]:
                    cnt+=1
                    nx+=dx[_]
                    ny+=dy[_]
                if cnt==5:
                    if 0 <=i-dy[_]<19 and 0<=j-dx[_]<19:
                        if board[i][j]==board[i-dy[_]][j-dx[_]]:
                            continue
                        else:
                            ans.append([board[i][j],i+1,j+1])
                            flag=True
                            break
                    else:
                        ans.append([board[i][j], i + 1, j + 1])
                        flag = True
                        break
        if flag:
            break
    if flag:
        break

if not ans:
    print(0)
else:
    print(ans[0][0])
    print(ans[0][1],ans[0][2])

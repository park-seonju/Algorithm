def solution(rows, columns, queries):
    board=[[0]*(rows+2)]+[[0]+[0 for _ in range(columns)]+[0] for _ in range(rows)]+[[0]*(rows+2)]
    k=1
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            board[i][j]=k
            k+=1
    answer=[]
    for i in queries:
        x1,y1,x2,y2=i[0],i[1],i[2],i[3] #1 1 6 3
        temp=board[x1][y1]
        garo=y2-y1;sero=x2-x1  # 2 5
        for c in range(1,garo+1):
            temp=min(temp,board[x1][y1+c])
            board[x1][y1],board[x1][y1+c]=board[x1][y1+c],board[x1][y1]
        for r in range(1,sero+1):
            temp=min(temp,board[x1+r][y1+garo])
            board[x1][y1],board[x1+r][y1+garo]=board[x1+r][y1+garo],board[x1][y1]
        for c in range(1,garo+1):
            temp=min(temp,board[x2][y2-c])
            board[x1][y1],board[x2][y2-c]=board[x2][y2-c],board[x1][y1]
        for r in range(1,sero+1):
            temp=min(temp,board[x2-r][y1])
            board[x1][y1],board[x2-r][y1]=board[x2-r][y1],board[x1][y1]
        answer.append(temp)
    return answer
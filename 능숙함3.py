def check(a,b):
    #1.  소 소 / 대 대 / 대 소 / 소 대
    if a.isupper() and b.isupper() and a==b :return True
    if a.islower() and b.islower() and a == b:return True
    if a.isupper() and b.islower() and a == b.upper(): return True
    if a.islower() and b.isupper() and a.upper() == b : return True
    return False
def solution(m, n, board):
    answer = 0
    info=[['' for a in range(n)] for aa in range(m)]
    for i in range(m):
        for j in range(n):
            info[i][j]=board[i][j]
    
    while 1:
        changeFlag=False    
        for i in range(m-1):
            for j in range(n-1):
                if info[i][j] != ' ' and check(info[i][j],info[i][j+1]) and check(info[i][j], info[i+1][j]) and check(info[i][j],info[i+1][j+1]):
                    if info[i][j].isupper(): 
                        answer+=1
                        info[i][j] = info[i][j].lower()
                    if info[i][j+1].isupper():
                        answer+=1
                        info[i][j+1] = info[i][j+1].lower()
                    if info[i+1][j].isupper():
                        answer+=1
                        info[i+1][j] = info[i+1][j].lower()
                    if info[i+1][j+1].isupper():
                        answer+=1
                        info[i+1][j+1] = info[i+1][j+1].lower()
                    changeFlag=True
        if changeFlag:
            for i in range(n):
                for j in range(m-2,-1,-1):
                    for k in range(j,m-1):
                        if info[k + 1][i] == ' ' or info[k + 1][i].islower():
                            info[k + 1][i] = info[k][i];
                            info[k][i] = ' ';
                        else: break
        else:break
    return answer
solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])
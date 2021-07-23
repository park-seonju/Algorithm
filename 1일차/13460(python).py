import queue

r,c = map(int, input().split())
map = [list(map(str, input().strip())) for _ in range(r)]
visited = [[[[False for _ in range(c)] for _ in range(r)] for _ in range(c)] for _ in range(r)]
def makeAnswer() :
    for i in range(r) :
        for j in range(c) :
            if map[i][j]=='R' :
                rR,rC=i,j
                map[i][j]='.'
            elif map[i][j]=='B' :
                bR,bC=i,j
                map[i][j]='.'
    
    que = queue.Queue()
    que.put([rR, rC, bR, bC, 0])
    finish = False
    ans=-1
    
    while not que.empty() and not finish :
        
        now = que.get()
        
        if now[4]>=10 or visited[now[0]][now[1]][now[2]][now[3]] : continue
        visited[now[0]][now[1]][now[2]][now[3]]=True
        
        for i in range(4) :
            rR2, rC2, bR2, bC2, count = now
            if i==0 :                                    #아래쪽
                while map[rR2+1][rC2]=='.' : rR2+=1
                while map[bR2+1][bC2]=='.' : bR2+=1

                if map[bR2+1][bC2]=='O' : continue
                
                if rC2==bC2 :
                    if map[rR2+1][rC2]=='O' :
                        ans=now[4]+1
                        finish=True
                        break
                    if rR2==bR2 and now[0]<now[2] : rR2-=1
                    elif rR2==bR2 and now[0]>now[2] : bR2-=1
                else :
                    if map[rR2+1][rC2]=='O' :
                        ans=now[4]+1
                        finish=True
                        break
                que.put([rR2,rC2,bR2,bC2,count+1])

            elif i==1 :                                    #위쪽
                while map[rR2-1][rC2]=='.' : rR2-=1
                while map[bR2-1][bC2]=='.' : bR2-=1

                if map[bR2-1][bC2]=='O' : continue
                
                if rC2==bC2 :
                    if map[rR2-1][rC2]=='O' :
                        ans=now[4]+1
                        finish=True
                        break
                    if rR2==bR2 and now[0]<now[2] : bR2+=1
                    elif rR2==bR2 and now[0]>now[2] : rR2+=1
                else :
                    if map[rR2-1][rC2]=='O' :
                        ans=now[4]+1
                        finish=True
                        break
                que.put([rR2,rC2,bR2,bC2,count+1])
                
            elif i==2 :                                    #왼쪽
                while map[rR2][rC2-1]=='.' : rC2-=1
                while map[bR2][bC2-1]=='.' : bC2-=1

                if map[bR2][bC2-1]=='O' : continue
                if rR2==bR2 :
                    if map[rR2][rC2-1]=='O' :
                        ans=now[4]+1
                        finish=True
                        break
                    if rC2==bC2 and now[1]<now[3] : bC2+=1
                    elif rC2==bC2 and now[1]>now[3] : rC2+=1
                else :
                    if map[rR2][rC2-1]=='O' :
                        ans=now[4]+1
                        finish=True
                        break
                que.put([rR2,rC2,bR2,bC2,count+1])
                
            elif i==3 :                                    #오른쪽
                while map[rR2][rC2+1]=='.' : rC2+=1
                while map[bR2][bC2+1]=='.' : bC2+=1

                if map[bR2][bC2+1]=='O' : continue

                if rR2==bR2 :
                    if map[rR2][rC2+1]=='O' :
                        ans=now[4]+1
                        finish=True
                        break
                    if rC2==bC2 and now[1]<now[3] : rC2-=1
                    elif rC2==bC2 and now[1]>now[3] : bC2-=1
                else :
                    if map[rR2][rC2+1]=='O' :
                        ans=now[4]+1
                        finish=True
                        break
                que.put([rR2,rC2,bR2,bC2,count+1])
    print(ans)

makeAnswer()
                    
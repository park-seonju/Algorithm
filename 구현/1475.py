import sys
input=sys.stdin.readline
N=input()
six_nine=['6','9']
check=['1','2','3','4','5','6','7','8','9','0']
check_list=[]
cnt=0   # 처음엔 cnt를 숫자로만 하려했음
for i in range(len(N)-1):
    if N[i] in six_nine: # '6또는 9임'
        check_list.append(N[i])
        if (check_list.count('6')+check_list.count('9'))>2 and (check_list.count('6')+check_list.count('9'))%2 == 1  : #체크리스트의 6,9가 있으면
            cnt+=1
    else:
        if N[i] in check_list:
            cnt+=1
        check_list.append(N[i])
print('check_list',check_list)
print('cnt',cnt)







N=list(map(int,input().strip()))    # 끝 공백만 지울땐 strip
six_nine=[6,9]
cnt=[0]*9 
for i in N:
    if i in six_nine: # '6또는 9임'
        cnt[6]+=1
    else:
        cnt[i]+=1
        
if cnt[6]%2 == 0:  # 6,9가 1,2 => 1  3,4 => 2  5,6 => 3개 이므로
    cnt[6]//=2
else:
    cnt[6]=(cnt[6]//2)+1 
print(max(cnt))


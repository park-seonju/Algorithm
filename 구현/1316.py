import sys
input=sys.stdin.readline
N=int(input())
# 못품

ans=0
for _ in range(N):
    cnt=0
    word=input()
    for i in range(len(word)-1):    
        if word[i]!=word[i+1]: #다르면 즉 0번 1번 비교후 2번부터 끝까지 0이 있는지 // 같으면 상관없음
            back_word=word[i+1:]
            if back_word.count(word[i]):
                cnt+=1
    if cnt==0:
        ans+=1
print(ans)
#
'''
import sys

input = sys.stdin.readline

n = int(input())

ans=0
for case in range(n):
    word = input().strip()
    check_alpha = ''
    for alpha in word:
        # 체크알파 안에 알파벳이 있는가.
        if alpha not in check_alpha:
            #없으면 그냥 넣어준다.
            check_alpha += alpha
        # 있으면 두가지로 나뉜다. 바로 전에랑 같은가 다른가.
        else:
            # 같으면 그대로 넣어준다.
            if alpha == check_alpha[-1]:
                check_alpha += alpha
            # 다르면 그 즉시 반복문을 종료한다.
            else:
                break
    # 체크알파와 처음 단어가 같으면 그 단어는 추가해주고
    if len(check_alpha) == len(word):
        ans +=1
    # 아니면 pass 한다.
    else:
        pass
        
print(ans)
'''
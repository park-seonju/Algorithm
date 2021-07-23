from collections import deque
S=deque(list(input()))
ans=[]
word = S.popleft()
while S:
    temp = ""
    if word == '<':
        flag=True
        while flag:
            if len(S)==0:
                break
            ans.append(word)
            word=S.popleft()
            if word == '>':
                ans.append(word)
                flag = False
                if len(S) == 0:
                    break
                word = S.popleft()
    else:
        while word != ' ' and word != '<':
            temp += word
            if len(S)==0:
                break
            word=S.popleft()
        ans.append(temp[::-1])
        if word==' ':
            ans.append(word)
            if len(S)==0:
                break
            word = S.popleft()
for i in ans:
    print(i,end="")
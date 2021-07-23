L,C=map(int,input().split())
word=list(input().split())
word.sort()
ans=[0]*L
def func(idx,start,ja,mo):
    if idx==L:
        if ja>=2 and mo>=1:
            print(''.join(ans))
        return
    for i in range(start,C):
        ans[idx]=word[i]
        if word[i] in ['a','e','i','o','u']:
            mo+=1
            func(idx+1,i+1,ja,mo)
            mo-=1
        else:
            ja+=1
            func(idx+1,i+1,ja,mo)
            ja-=1
func(0,0,0,0)
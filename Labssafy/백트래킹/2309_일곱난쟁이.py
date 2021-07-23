def bt(n,start,total):
    if n==7 and sum(total)==100:
        total.sort()
        for i in total:
            print(i)
        exit()
    elif n>7 or sum(total)>100:return
    for i in range(start,9):
        total.append(num[i])
        bt(n+1,start+1,total)
        total.pop()

num=[int(input()) for _ in range(9)]
bt(0,0,[])
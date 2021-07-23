Test=int(input())
for tc in range(Test):
    th=int(input())
    score_list=list(map(int,input().split()))
    dic={}
    for num in score_list:
        dic[num]=dic.get(num,0)+1
    sort_dic=sorted(dic.items(),key=(lambda x:x[1]),reverse=True)
    maxcnt=sort_dic[0][1]
    maxnum=0
    if sort_dic[0][0]==sort_dic[0][1]:
        for i in sort_dic:
            if i[1]==maxcnt:
                maxnum=i[0]
        print("#{} {}".format(th,maxnum))
    else:
        print("#{} {}".format(th,sort_dic[0][0]))

    
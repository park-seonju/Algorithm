def solution(lottos, win_nums):
    prize={0:6,1:6,2:5,3:4,4:3,5:2,6:1}
    answer = []
    cnt=0
    zero=0
    for i in lottos:
        if i:
            for j in win_nums:
                if i==j:
                    cnt+=1
        else:
            zero+=1
    answer.append(prize[cnt+zero])
    answer.append(prize[cnt])
    return answer
def solution(answers):
    answer = []
    one=0
    two=0
    three=0
    check=0
    check_three=0
    for i in range(len(answers)):
        if i%5==0 and answers[i]==1:one+=1
        elif i%5==1 and answers[i]==2:one+=1
        elif i%5==2 and answers[i]==3:one+=1
        elif i%5==3 and answers[i]==4:one+=1
        elif i%5==4 and answers[i]==5:one+=1
        if i%2==0 and answers[i]==2: two+=1
        if i%2:
            if check==0 and answers[i]==1:two+=1
            elif check==1 and answers[i]==3:two+=1
            elif check==2 and answers[i]==4:two+=1
            elif check==3 and answers[i]==5:two+=1
            check+=1
        if check_three==0 and answers[i]==3:three+=1
        elif check_three==1 and answers[i]==1:three+=1
        elif check_three==2 and answers[i]==2:three+=1
        elif check_three==3 and answers[i]==4:three+=1
        elif check_three==4 and answers[i]==5:three+=1
        if check==4:check=0
        if i%2:
            check_three+=1
            if check_three==5:check_three=0
    num_list=[]
    num_list.append(one)
    num_list.append(two)
    num_list.append(three)
    for i in range(3):
        if num_list[i] == max(one,two,three):
            answer.append(i+1)
    return answer

solution([1,3,2,4,2]	)
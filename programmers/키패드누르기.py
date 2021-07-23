def solution(numbers, hand):
    answer = ''
    left=[0]*8
    right=[0]*10
    left_num=0
    right_num=0
    for num in numbers:
        if num==1 or num==4 or num==7:
            left_num=num
            answer+='L'
        elif num==3 or num==6 or num==9:
            right_num=num
            answer+='R'
        else:
            pass
                
    return answer
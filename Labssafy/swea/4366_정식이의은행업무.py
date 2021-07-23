T=int(input())
for tc in range(1,T+1):
    binary=input().rstrip()
    three=input().rstrip()
    binary_list=[]
    three_list=[]
    for i in range(len(binary)):
        if binary[i]=='0':
            new=binary[:i]+'1'+binary[i+1:]
            binary_list.append(new)
        else:
            new=binary[:i]+'0'+binary[i+1:]
            binary_list.append(new)

    for i in range(len(three)):
        if three[i]=='0':
            new=three[:i]+'1'+three[i+1:]
            three_list.append(new)
            new=three[:i]+'2'+three[i+1:]
            three_list.append(new)
        elif three[i]=='1':
            new=three[:i]+'0'+three[i+1:]
            three_list.append(new)
            new=three[:i]+'2'+three[i+1:]
            three_list.append(new)
        elif three[i]=='2':
            new=three[:i]+'1'+three[i+1:]
            three_list.append(new)
            new=three[:i]+'0'+three[i+1:]
            three_list.append(new)
    flag=False
    for binum in binary_list:
        for threenum in three_list:
            if int(binum,2)==int(threenum,3):
                print("#{} {}".format(tc,int(binum,2)))
                flag=True;break
        if flag: break





# for i in all_list:
#     check_num=int(i,2)
#     print(check_num)
#     three_change=''
#     while check_num:
#         remain=check_num%3
#         check_num=check_num//3
#         three_change=str(remain)+three_change
#         if check_num<3:
#             three_change=str(check_num)+three_change
#     print(three_change)
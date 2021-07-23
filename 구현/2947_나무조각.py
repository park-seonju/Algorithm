my_list=list(map(int,input().split()))
ans=[1,2,3,4,5]
result=[]
while my_list != ans:
    if my_list[0] > my_list[1]:
        my_list[0],my_list[1] = my_list[1],my_list[0]
        print(*my_list)
    if my_list[1] > my_list[2]:
        my_list[1], my_list[2] = my_list[2], my_list[1]
        print(*my_list)
    if my_list[2] > my_list[3]:
        my_list[2], my_list[3] = my_list[3], my_list[2]
        print(*my_list)
    if my_list[3] > my_list[4]:
        my_list[3], my_list[4] = my_list[4], my_list[3]
        print(*my_list)